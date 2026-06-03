# app/services/chat/chatbot.py

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.services.chat.retriever import get_retriever
from app.core.config import settings

def build_chatbot():
    llm = OllamaLLM(model=settings.LLM_MODEL)
    retriever = get_retriever()

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=f"{settings.SYSTEM_PROMPT}\n\nContext: {{context}}\n\nQuestion: {{question}}\n\nAnswer:"
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def chain_invoke(question):
        docs = retriever.invoke(question)
        context = format_docs(docs)
        filled_prompt = prompt.format(context=context, question=question)
        response = llm.invoke(filled_prompt)
        return StrOutputParser().invoke(response)

    return chain_invoke

def chat(chain, question):
    return chain(question)