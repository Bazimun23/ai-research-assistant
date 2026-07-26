from fastapi import APIRouter
from pydantic import BaseModel

from src.vector_store.manager import VectorStore

router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"]
)


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@router.post("/")
def semantic_search(request: SearchRequest):

    vector_store = VectorStore()

    results = vector_store.search(
        query=request.query,
        top_k=request.top_k
    )

    return results