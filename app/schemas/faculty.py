from pydantic import BaseModel, EmailStr
from typing import Optional


class FacultyBase(BaseModel):
    full_name: Optional[str] = None
    designation: Optional[str] = None
    department: Optional[str] = None
    university: Optional[str] = None
    email: Optional[EmailStr] = None
    bio: Optional[str] = None
    profile_image: Optional[str] = None


class FacultyUpdate(FacultyBase):
    pass


class FacultyOut(FacultyBase):
    id: int

    class Config:
        from_attributes = True