import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DEBUG = os.getenv("DEBUG")
    DATA_FILE = os.getenv("DATA_FILE")

    # RAG
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
    LLM_MODEL = os.getenv("LLM_MODEL", "gemma4:31b-cloud")
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "hrms_docs")
    VECTORSTORE_DIR = os.getenv("VECTORSTORE_DIR", "vectorstore")
    DATA_DIR = os.getenv("DATA_DIR", "data")

    SYSTEM_PROMPT = """You are a friendly HRMS assistant.
For greetings or small talk, respond naturally and politely.
For HRMS questions, answer only from the provided context, be concise and direct.
If HRMS information is not in context, say 'I don't have that information.'"""

    # Database
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "hrms_chatbot")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "root")


settings = Settings()