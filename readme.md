# Advanced PDF-Based RAG System | Custom Knowledge Retrieval & AI Chat

This repository contains a modular, production-ready **Retrieval-Augmented Generation (RAG)** application built with Python. The system allows users to upload unstructured PDF documents and interact with them through a conversational AI interface, providing precise, context-grounded answers with source citations.

## 🚀 Key Features

- **Modular Architecture:** Clean separation of concerns across ingestion, embedding, vector storage, retrieval, and generation modules.
- **Smart Document Ingestion:** Automated pipeline for loading, cleaning, and recursive chunking of complex PDF layouts to maintain context.
- **High-Performance Vector Search:** Integrated **FAISS** (Facebook AI Similarity Search) for millisecond-latency retrieval of relevant document segments.
- **Context-Grounded Generation:** Leverages **LangChain** to connect custom retrievers with state-of-the-art LLMs (OpenAI/Hugging Face), eliminating hallucinations.
- **Interactive UI:** A sleek and responsive web interface built with **Streamlit** for real-time document querying and chat history.

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Frameworks:** LangChain, Streamlit
- **Vector Database:** FAISS
- **AI Models:** OpenAI GPT / Hugging Face Transformers
- **Data Processing:** PyPDF2, TikToken

## 📁 Project Structure

```text
├── embedding/      # Logic for generating text embeddings
├── generation/     # LLM integration and response synthesis
├── ingestion/      # PDF loading and text preprocessing
├── retriever/      # Custom retrieval logic and search optimization
├── vector_db/      # Vector database management (FAISS)
├── app.py          # Main Streamlit application entry point
└── requirements.txt # Project dependencies
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AwaisAhmed183/pdf-rag-streamlit-app.git
   cd pdf-rag-streamlit-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file and add your API keys:
   ```text
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📝 Usage

1. Upload a PDF file via the sidebar.
2. Wait for the system to process and index the document.
3. Start chatting with your PDF in the main window!

---
**Author:** [Awais Ahmed Shah](https://github.com/AwaisAhmed183)  
**Specialization:** Data Science | Machine Learning | NLP | RAG Engineer
