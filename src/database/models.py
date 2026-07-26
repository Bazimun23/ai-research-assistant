from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from .base import Base


class Document(Base):
    __tablename__ = "documents"

    doc_id = Column(String, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=True)

    upload_timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    total_pages = Column(Integer, default=0)
    total_chunks = Column(Integer, default=0)

    processing_status = Column(
        String,
        default="PENDING"
    )

    category = Column(
        String,
        default="Unknown"
    )