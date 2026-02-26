from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    publisher: Optional[str] = None
    year: int
    isbn: Optional[str] = None
    doi: Optional[str] = None
    category: Optional[str] = None
    cover_image: Optional[str] = None
    official_url: Optional[str] = None  # ✅ MUST BE HERE


class BookCreate(BookBase):
    faculty_id: int


class BookUpdate(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    year: Optional[int] = None
    isbn: Optional[str] = None
    doi: Optional[str] = None
    category: Optional[str] = None
    cover_image: Optional[str] = None
    official_url: Optional[str] = None  # ✅ ALSO HERE


class BookOut(BookBase):
    id: int
    faculty_id: int

    class Config:
        from_attributes = True