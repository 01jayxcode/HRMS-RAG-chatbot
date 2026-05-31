from langchain_community.vectorstores import Chroma
from pipeline.loader import laod_documents
from pipeline.splitter import split_documents
from pipeline.embedder import get_embeddings
from config.settings import VECTORSTORE_DIR, COLLECTION_NAME


def ingest():

    print("Step 1: Loading PDFs...")
    documents = laod_documents()

    print("\nStep 2: Splitting into chunks...")
    chunks = split_documents(documents)

    print("\nStep 3: Loading embedding model...")
    embeddings = get_embeddings()

    print("\nStep 4: Saving to ChromaDB...")
    
    vectorstore = Chroma.from_documents(

        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=VECTORSTORE_DIR
    )

    print(f"\nDone. {len(chunks)} chunks saved to vectorstore.")
    return vectorstore

    
