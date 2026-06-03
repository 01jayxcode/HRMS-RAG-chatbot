# app/services/rag_service.py

from app.services.pipeline.ingestor import ingest
from app.services.chat.chatbot import build_chatbot
from app.core.config import settings
from app.db.chat_repository import save_message, get_history
import os

class RAGService:
    def __init__(self):
        self.chain = None

    def initialize(self):
        if not os.path.exists(settings.VECTORSTORE_DIR) or not os.listdir(settings.VECTORSTORE_DIR):
            ingest()
        self.chain = build_chatbot()

    def ask(self, question: str, session_id: str) -> str:
        if self.chain is None:
            raise RuntimeError("RAG service not initialized.")

        history = get_history(session_id)

        history_text = ""
        for msg in history:
            if msg["role"] == "user":
                history_text += f"User: {msg['content']}\n"
            else:
                history_text += f"Assistant: {msg['content']}\n"

        full_question = f"{history_text}User: {question}" if history_text else question

        # call chain directly as function
        answer = self.chain(full_question)

        save_message(session_id, "user", question)
        save_message(session_id, "assistant", answer)

        return answer

    def re_ingest(self) -> dict:
        result = ingest()
        self.chain = build_chatbot()
        return result

rag_service = RAGService()