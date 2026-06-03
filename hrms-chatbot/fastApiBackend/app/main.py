# main.py

from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.chat_routes import router as chat_router
from app.core.config import settings
from app.services.rag_service import rag_service


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(chat_router)

@app.on_event("startup")
async def startup_event():
    print("Initializing RAG service...")
    rag_service.initialize()
    print("RAG service ready.")