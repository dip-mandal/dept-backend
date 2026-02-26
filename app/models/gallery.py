# backend/app/models/gallery.py

from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
# from app.db.base import Base
from app.db.base_class import Base


class Gallery(Base):
    __tablename__ = "gallery"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    media_url = Column(String, nullable=False)
    media_type = Column(String, nullable=False)  # image / video

    created_at = Column(DateTime, default=datetime.utcnow)