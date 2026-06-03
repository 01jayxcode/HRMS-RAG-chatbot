# app/services/pipeline/ingestor.py

from langchain_chroma import Chroma
from app.services.pipeline.loader import load_documents
from app.services.pipeline.splitter import split_documents
from app.services.pipeline.embedder import get_embeddings
from app.core.config import settings

def ingest():
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=settings.COLLECTION_NAME,
        persist_directory=settings.VECTORSTORE_DIR
    )

    return {"chunks_ingested": len(chunks)}