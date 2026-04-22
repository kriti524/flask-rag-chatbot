# flask-rag-chatbot
A Retrieval-Augmented Generation (RAG) chatbot built with Flask, ChromaDB, Sentence-Transformers embeddings, and FLAN-T5 for document-based semantic question answering.
# 🚀 RAG Chatbot using Flask + ChromaDB + Transformers

This project is a Retrieval-Augmented Generation (RAG) system that allows users to ask questions based on custom documents. It combines semantic search using embeddings with a large language model (FLAN-T5) to generate accurate, context-aware answers.

# 🧠 How it works

User Question → Sentence Transformer (Embeddings) → ChromaDB Vector Search → Relevant Documents Retrieved → FLAN-T5 LLM → Final Answer

# ⚙️ Features
- Ask questions from your own documents
- Semantic search using embeddings
- Vector database (ChromaDB)
- LLM-based answer generation (FLAN-T5)
- Flask REST API backend
- Supports multiple text files in docs folder

# 🧱 Tech Stack
Python, Flask, Sentence-Transformers, ChromaDB, Hugging Face Transformers, FLAN-T5

# 📁 Project Structure
rag-llm-app/
├── app.py (Flask API)
├── rag.py (Retrieval logic)
├── llm.py (LLM inference)
├── ingest.py (Document ingestion)
├── docs/ (Knowledge base files)
└── requirements.txt

# 📚 Knowledge Base
Place all .txt files inside the docs/ folder. These files are converted into embeddings and stored in ChromaDB for semantic search.

# ⚙️ Setup
1. pip install -r requirements.txt  
2. python ingest.py  
3. python app.py  

Server runs at: http://localhost:5001

# 🧪 API Usage
curl -X POST http://localhost:5001/ask -H "Content-Type: application/json" -d '{"question": "What is RAG?"}'

# 📊 Output Example
{
  "question": "What is RAG?",
  "answer": "RAG is a system that retrieves relevant documents and uses them to generate answers.",
  "sources": ["retrieved context from docs"]
}

# 🧠 Core Concepts
Embeddings convert text into vectors for semantic search. ChromaDB stores these vectors. RAG retrieves relevant context and passes it to the LLM to generate accurate answers.

# 🚀 Future Improvements
Add UI (Streamlit/React), improve chunking, add reranking, deploy to cloud.

# 👨‍💻 Author
Built as a learning project to understand RAG systems, vector databases, and LLM integration.
