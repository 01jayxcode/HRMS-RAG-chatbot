# app/services/pipeline/embedder.py

from langchain_ollama import OllamaEmbeddings
from app.core.config import settings

def get_embeddings():
    embeddings = OllamaEmbeddings(
        model=settings.EMBEDDING_MODEL
    )
    return embeddings