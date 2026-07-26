from src.vector_store.manager import VectorStore
from src.database.base import SessionLocal
from src.database.models import Document

from src.document_processing.pdf_parser import PDFProcessor
from src.document_processing.chunker import TextChunker

from fastapi import APIRouter, UploadFile, File, HTTPException

import os
import shutil
import uuid


router = APIRouter(
    prefix="/documents",
    tags=["Document Management"]
)


UPLOAD_DIR = "data/raw_documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)


# Upload Document
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )


    doc_id = str(uuid.uuid4())


    file_path = os.path.join(
        UPLOAD_DIR,
        f"{doc_id}_{file.filename}"
    )


    # Save PDF file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)



    db = SessionLocal()


    # Create document record
    document = Document(
        doc_id=doc_id,
        file_name=file.filename,
        file_path=file_path,
        processing_status="PROCESSING"
    )


    db.add(document)
    db.commit()



    try:

        # PDF Text Extraction
        pdf_processor = PDFProcessor()

        result = pdf_processor.extract_text(file_path)


        total_pages = result["total_pages"]

        pages = result["pages"]



        # Create Chunks
        chunker = TextChunker()

        chunks = chunker.create_chunks(pages)


        total_chunks = len(chunks)

        # Store chunks in ChromaDB
        vector_store = VectorStore()
        vector_store.add_chunks(
            doc_id=doc_id,
            chunks=chunks
        )

        # Update metadata
        document.total_pages = total_pages
        document.total_chunks = total_chunks
        document.processing_status = "PROCESSED"


        db.commit()



    except Exception as e:

        document.processing_status = "FAILED"

        db.commit()

        db.close()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


    db.close()



    return {
        "message": "PDF uploaded and processed successfully",
        "document_id": doc_id,
        "filename": file.filename,
        "total_pages": total_pages,
        "total_chunks": total_chunks,
        "status": "PROCESSED"
    }




# List Documents
@router.get("/")
def list_documents():

    db = SessionLocal()

    documents = db.query(Document).all()

    db.close()

    return documents




# Delete Document
@router.delete("/{doc_id}")
def delete_document(doc_id: str):

    db = SessionLocal()


    document = (
        db.query(Document)
        .filter(Document.doc_id == doc_id)
        .first()
    )


    if not document:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )



    # Delete PDF file
    if document.file_path and os.path.exists(document.file_path):

        os.remove(document.file_path)



    # Delete database record
    db.delete(document)

    db.commit()

    db.close()



    return {
        "message": "Document deleted successfully",
        "document_id": doc_id
    }


