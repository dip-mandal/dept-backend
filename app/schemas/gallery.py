from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GalleryBase(BaseModel):
    title: str
    description: Optional[str] = None
    media_url: str
    media_type: str


class GalleryCreate(GalleryBase):
    pass


class GalleryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    media_url: Optional[str] = None
    media_type: Optional[str] = None


class GalleryOut(GalleryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True