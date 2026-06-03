# app/services/chat/retriever.py

from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from app.services.pipeline.embedder import get_embeddings
from app.services.pipeline.loader import load_documents
from app.services.pipeline.splitter import split_documents
from app.core.config import settings

def get_retriever():
    embeddings = get_embeddings()

    # semantic retriever
    vectorstore = Chroma(
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=settings.VECTORSTORE_DIR
    )
    semantic_retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    # keyword retriever
    documents = load_documents()
    chunks = split_documents(documents)
    bm25_retriever = BM25Retriever.from_documents(chunks)
    bm25_retriever.k = 5

    # manual hybrid retriever
    class HybridRetriever:
        def invoke(self, question):
            semantic_results = semantic_retriever.invoke(question)
            bm25_results = bm25_retriever.invoke(question)

            # combine and deduplicate
            seen = set()
            combined = []
            for doc in semantic_results + bm25_results:
                if doc.page_content not in seen:
                    seen.add(doc.page_content)
                    combined.append(doc)

            return combined[:5]

    return HybridRetriever()