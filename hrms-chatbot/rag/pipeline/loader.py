from langchain_community.document_loaders import PyPDFLoader
from config.settings import DATA_DIR
import os

def laod_documents():
    documents=[]
    pdf_files=[f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]

    if not pdf_files:
        raise ValueError(f"No PDF files found in {DATA_DIR}")
    
    for pdf_file in pdf_files:
        pdf_path=os.path.join(DATA_DIR,pdf_file)
        loader=PyPDFLoader(pdf_path)
        docs=loader.load()
        documents.extend(docs)
        print(f"Loaded: {pdf_file} — {len(docs)} pages")

    
    
    print(f"\nTotal documents loaded: {len(documents)}")
    return documents
