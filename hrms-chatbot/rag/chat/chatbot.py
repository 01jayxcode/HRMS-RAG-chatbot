# chat/chatbot.py

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from chat.retriever import get_retriever
from config.settings import LLM_MODEL, SYSTEM_PROMPT

def build_chatbot():
    llm = OllamaLLM(model=LLM_MODEL)
    retriever = get_retriever()

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=f"{SYSTEM_PROMPT}\n\nContext: {{context}}\n\nQuestion: {{question}}\n\nAnswer:"
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

def chat(chain, question):
    return chain.invoke(question)