from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProjectBase(BaseModel):
    title: str
    funding_agency: Optional[str] = None
    amount: Optional[float] = None
    role: Optional[str] = None  # PI / Co-PI
    duration: Optional[str] = None
    status: Optional[str] = None  # ongoing / completed
    description: Optional[str] = None
    faculty_id: int


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    funding_agency: Optional[str] = None
    amount: Optional[float] = None
    role: Optional[str] = None
    duration: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None


class ProjectOut(ProjectBase):
    id: int

    class Config:
        from_attributes = True
