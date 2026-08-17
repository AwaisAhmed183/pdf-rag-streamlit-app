import streamlit as st
import os
import tempfile
import hashlib
from dotenv import load_dotenv

#pipeline modules
from ingestion.loader import load_and_chunk_pdf
from embedding.embedder import get_embedder
from vector_db.faiss_db import create_vector_store
from retriever.context_retriever import setup_retriever
from generation.answer_generator import generate_answer

load_dotenv()

# Cache
@st.cache_resource(show_spinner = False)
def _build_vector_store_from_pdf_bytes(
    pdf_bytes: bytes,
    chunk_size: int,
    chunk_overlap: int,
    embedding_model_name: str,
):
    with tempfile.NamedTemporaryFile(delete = False, suffix = ".pdf") as tmp_file:
        tmp_file.write(pdf_bytes)
        tmp_path = tmp_file.name


    try:
        chunks = load_and_chunk_pdf(
            tmp_path,
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap
        )

        embed_model = get_embedder(model_name=embedding_model_name)

        v_store = create_vector_store(chunks, embed_model)

        return v_store, len(chunks)

    finally:
        os.remove(tmp_path)

## UI

st.set_page_config(page_title = "Chat With PDF", page_icon = "📚")

st.title("📚 Chat With PDF")
st.caption("Chat with your PDF documents using Ollamaa...")


# Session states
if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "pipeline_key" not in st.session_state:
    st.session_state.pipeline_key = 0

if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:
    st.header("Document Setup")
    uploaded_file = st.file_uploader("Upload a PDF File", type = "pdf")
    chunk_size = st.number_input("Chunk Size", 200, 5000, 500, step = 100)
    chunk_overlap = st.number_input("Chunk Overlap", 0, 1000, 50, step = 50)

    embedding_model_name = st.text_input(
        "Embedding Model",
        value = "sentence-transformers/all-MiniLM-L6-v2",
    )

    st.header("Model Settings")
    model_name = st.selectbox(
        "Ollama Model",
        options = [
            "qwen2.5:3b",   # fast
            "qwen2.5:0.5b",
            "llama3:8b",
            "mistral:7b",
        ]
    )

    build_btn = st.button("Build Pipeline")

    # Build Pipeline

    if uploaded_file and build_btn:
        with st.spinner("Building Pipeline..."):
            pdf_bytes = uploaded_file.getvalue()
            pdf_hash = hashlib.sha256(pdf_bytes).hexdigest()

            pipeline_key = f"{pdf_hash}:{chunk_size}:{chunk_overlap}:{embedding_model_name}"

            if st.session_state.pipeline_key != pipeline_key:
                st.session_state.retriever = None
            st.session_state.pipeline_key = pipeline_key
            st.session_state.messages = []  # reset chat on new doc

        v_store, chunk_count = _build_vector_store_from_pdf_bytes(
            pdf_bytes=pdf_bytes,
            chunk_size=int(chunk_size),
            chunk_overlap=int(chunk_overlap),
            embedding_model_name=embedding_model_name,
        )

        st.session_state.retriever = setup_retriever(v_store)
        st.sidebar.success(f"✅ Ready! {chunk_count} chunks created.")

# ---------------- Display Chat ---------------- #
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------------- User Input ---------------- #
user_input = st.chat_input("Ask something about your document...")

if user_input:
    if st.session_state.retriever is None:
        st.warning("Please upload and process a PDF first.")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                answer = generate_answer(
                    retriever=st.session_state.retriever,
                    query=user_input,
                    model_name=model_name,
                )

                st.markdown(answer)

        # Save assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )