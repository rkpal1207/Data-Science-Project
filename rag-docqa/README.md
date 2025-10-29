# 📚 Document Search & Question Answering (RAG System)

A Retrieval-Augmented Generation (RAG) pipeline built using Python, ChromaDB, BM25, and FastAPI.

## 🚀 Features
- Ingests and chunks PDFs
- Embeds text using SentenceTransformers
- Hybrid retrieval (BM25 + semantic)
- LLM-powered or mocked QA responses
- FastAPI & Streamlit front-ends

## 🧩 Architecture
Loader → Chunker → Embedder → Indexer → Retriever → LLM → API/UI
