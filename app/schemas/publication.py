from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.publication import PublicationType


class PublicationBase(BaseModel):
    title: str
    authors: str
    publication_type: PublicationType
    year: int
    journal_name: Optional[str] = None
    publisher: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None
    impact_factor: Optional[float] = None
    is_scopus_indexed: Optional[bool] = False
    is_web_of_science: Optional[bool] = False
    pdf_url: Optional[str] = None
    faculty_id: int
    official_url: Optional[str] = None
    cover_image: Optional[str] = None
    abstract: Optional[str] = None


class PublicationCreate(PublicationBase):
    official_url: Optional[str] = None
    cover_image: Optional[str] = None
    abstract: Optional[str] = None


class PublicationUpdate(BaseModel):
    title: Optional[str] = None
    authors: Optional[str] = None
    year: Optional[int] = None
    publication_type: Optional[PublicationType] = None
    official_url: Optional[str] = None
    cover_image: Optional[str] = None
    abstract: Optional[str] = None


class PublicationOut(PublicationBase):
    id: int
    created_at: datetime
    official_url: Optional[str] = None
    cover_image: Optional[str] = None
    abstract: Optional[str] = None

    class Config:
        from_attributes = True
