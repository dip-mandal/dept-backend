from pydantic import BaseModel
from datetime import date
from typing import Optional


class AwardBase(BaseModel):
    title: str
    organization: str
    award_date: date
    description: Optional[str] = None


class AwardCreate(AwardBase):
    pass


class AwardUpdate(AwardBase):
    pass


class AwardOut(AwardBase):
    id: int

    class Config:
        from_attributes = True


class AwardListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    data: list[AwardOut]