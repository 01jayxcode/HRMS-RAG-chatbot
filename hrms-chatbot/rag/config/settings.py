import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "gemma4:31b-cloud"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

COLLECTION_NAME = "hrms_docs"

SYSTEM_PROMPT = """You are a friendly HRMS assistant. 
For greetings or small talk, respond naturally and politely.
For HRMS questions, answer only from the provided context, be concise and direct.
If HRMS information is not in context, say 'I don't have that information.'"""