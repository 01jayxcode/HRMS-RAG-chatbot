from langchain_ollama import OllamaEmbeddings
from config.settings import EMBEDDING_MODEL

def get_embeddings():
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )
    
    print(f"Embedding model loaded: {EMBEDDING_MODEL}")
    return embeddings
