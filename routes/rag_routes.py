from fastapi import APIRouter
from pydantic import BaseModel

from src.rag.rag_engine import RAGEngine

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_question(request: QuestionRequest):

    rag = RAGEngine()

    result = rag.ask(request.question)

    return result