from langchain_community.vectorstores import Chroma
from pipeline.embedder import get_embeddings
from config.settings import VECTORSTORE_DIR, COLLECTION_NAME

def get_retriever():
    embeddings = get_embeddings()
    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=VECTORSTORE_DIR
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}

    )

    print("Vectorstore loaded successfully.")
    return retriever