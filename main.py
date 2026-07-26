from fastapi import FastAPI

from src.database.base import Base, engine
from src.database import models

from routes.document_routes import router as document_router
from routes.search_routes import router as search_router
from routes.rag_routes import router as rag_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Research & Knowledge Assistant",
    description="Backend API for document processing, semantic search, RAG, and document classification",
    version="1.0.0"
)


# Register routers
app.include_router(document_router)
app.include_router(search_router)
app.include_router(rag_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Research & Knowledge Assistant",
        "status": "Running Successfully",
        "api_docs": "Open /docs for Swagger API documentation"
    }