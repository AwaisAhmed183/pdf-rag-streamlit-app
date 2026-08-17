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
