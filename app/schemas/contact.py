from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class ContactInfoBase(BaseModel):
    address: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    website: Optional[str]
    google_scholar: Optional[str]
    linkedin: Optional[str]


class ContactInfoUpdate(ContactInfoBase):
    pass


class ContactInfoOut(ContactInfoBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True


class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str


class ContactMessageOut(ContactMessageCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True