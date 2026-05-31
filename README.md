# HRMS Chatbot — RAG Pipeline

AI-powered HR assistant built with RAG (Retrieval Augmented Generation).

## Tech Stack
- **Backend**: FastAPI, LangChain, ChromaDB, PostgreSQL
- **AI**: Ollama (Gemma), nomic-embed-text embeddings
- **Search**: Hybrid search (Semantic + BM25)
- **Frontend**: React + Vite

## Setup

### Backend
cd backend
pip install -r requirements.txt
cp .env.example .env
# fill in your .env values
uvicorn app.main:app --reload

### Frontend
cd frontend
npm install
npm run dev

## Features
- PDF ingestion pipeline
- Semantic + keyword hybrid search
- Chat history with PostgreSQL
- Session management
- REST API
