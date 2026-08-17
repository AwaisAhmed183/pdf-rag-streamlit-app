from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedder(model_name = "sentence-transformers/all-MiniLM-L6-v2"):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    return embeddings