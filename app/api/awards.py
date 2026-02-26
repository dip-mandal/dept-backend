from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.award import AwardCreate, AwardUpdate, AwardOut, AwardListResponse
from app.crud import award as award_crud
from app.api.dependencies import get_current_user

router = APIRouter(prefix="/awards", tags=["Awards"])


@router.post("/", response_model=AwardOut)
def create_award(
    award: AwardCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return award_crud.create_award(db, award, faculty_id=1)


@router.get("/", response_model=AwardListResponse)
def list_awards(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    db: Session = Depends(get_db),
):
    total, awards = award_crud.get_awards(db, skip, limit, search)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": awards,
    }


@router.put("/{award_id}", response_model=AwardOut)
def update_award(
    award_id: int,
    award: AwardUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    updated = award_crud.update_award(db, award_id, award)
    if not updated:
        raise HTTPException(status_code=404, detail="Award not found")
    return updated


@router.delete("/{award_id}")
def delete_award(
    award_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    deleted = award_crud.delete_award(db, award_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Award not found")
    return {"message": "Award deleted"}