from pydantic import BaseModel
from typing import Optional
from datetime import date


class PatentBase(BaseModel):
    faculty_id: int
    title: str
    patent_type: Optional[str] = None
    application_number: Optional[str] = None
    registration_number: Optional[str] = None
    filing_date: Optional[date] = None
    publication_date: Optional[date] = None
    issue_date: Optional[date] = None
    inventors: Optional[str] = None
    status: Optional[str] = None


class PatentCreate(PatentBase):
    pass


class PatentUpdate(BaseModel):
    title: Optional[str]
    patent_type: Optional[str]
    application_number: Optional[str]
    registration_number: Optional[str]
    filing_date: Optional[date]
    publication_date: Optional[date]
    issue_date: Optional[date]
    inventors: Optional[str]
    status: Optional[str]


class PatentOut(PatentBase):
    id: int

    class Config:
        from_attributes = True