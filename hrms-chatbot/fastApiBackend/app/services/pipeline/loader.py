# app/services/pipeline/loader.py

from langchain_community.document_loaders import PyPDFLoader
from app.core.config import settings
import os

def load_documents():
    documents = []
    pdf_files = [f for f in os.listdir(settings.DATA_DIR) if f.endswith(".pdf")]

    if not pdf_files:
        raise ValueError(f"No PDF files found in {settings.DATA_DIR}")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(settings.DATA_DIR, pdf_file)
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        documents.extend(docs)

    return documents