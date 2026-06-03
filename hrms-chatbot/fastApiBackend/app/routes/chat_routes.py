# app/routes/chat_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag_service import rag_service
from app.db.chat_repository import create_session, get_history, session_exists


router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    question: str
    session_id: str = None

class ChatResponse(BaseModel):
    question: str
    answer: str
    session_id: str


@router.post("/session")
async def new_session():
    session_id = create_session()
    return {"session_id": session_id}

@router.post("/ask", response_model=ChatResponse)
async def ask(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    try:
         # create session if not provided
        if not request.session_id:
            session_id = create_session()
        elif not session_exists(request.session_id):
            raise HTTPException(status_code=404, detail="Session not found")
        else:
            session_id = request.session_id
        
        answer = rag_service.ask(request.question, session_id)

        return ChatResponse(question=request.question, answer=answer, session_id=session_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/history/{session_id}")
async def history(session_id: str):
    if not session_exists(session_id):
        raise HTTPException(status_code=404, detail="Session not found")
    messages = get_history(session_id)
    return {"session_id": session_id, "messages": messages}


@router.post("/ingest")
async def re_ingest():
    try:
        result = rag_service.re_ingest()
        return {"message": "Ingestion complete", "details": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health():
    return {"status": "ok", "chain_loaded": rag_service.chain is not None}