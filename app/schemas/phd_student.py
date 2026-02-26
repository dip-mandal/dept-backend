from pydantic import BaseModel
from typing import Optional
from datetime import date


class PhDStudentBase(BaseModel):
    name: str
    thesis_title: str
    university: Optional[str] = None
    role: Optional[str] = None
    award_date: Optional[date] = None
    status: Optional[str] = None  # completed / ongoing
    faculty_id: int
    
    profile_image: Optional[str] = None
    bio: Optional[str] = None
    research_area: Optional[str] = None


class PhDStudentCreate(PhDStudentBase):
    pass


class PhDStudentUpdate(BaseModel):
    name: Optional[str] = None
    thesis_title: Optional[str] = None
    university: Optional[str] = None
    role: Optional[str] = None
    award_date: Optional[date] = None
    status: Optional[str] = None


class PhDStudentOut(PhDStudentBase):
    id: int

    class Config:
        from_attributes = True
