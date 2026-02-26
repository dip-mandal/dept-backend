from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from app.api.deps import get_db
from app.models.patent import Patent
from app.schemas.patent import PatentCreate, PatentUpdate, PatentOut
from app.core.auth_guard import get_current_user

router = APIRouter()


@router.get("/")
def list_patents(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = None,
    patent_type: Optional[str] = None,
):
    query = db.query(Patent)

    if status:
        query = query.filter(Patent.status == status)

    if patent_type:
        query = query.filter(Patent.patent_type == patent_type)

    total = query.with_entities(func.count()).scalar()

    patents = (
        query.order_by(Patent.filing_date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": patents,
    }


@router.get("/{patent_id}", response_model=PatentOut)
def get_patent(patent_id: int, db: Session = Depends(get_db)):
    patent = db.query(Patent).filter(Patent.id == patent_id).first()
    if not patent:
        raise HTTPException(status_code=404, detail="Patent not found")
    return patent


@router.post("/", response_model=PatentOut)
def create_patent(
    patent_data: PatentCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    patent = Patent(**patent_data.dict())
    db.add(patent)
    db.commit()
    db.refresh(patent)
    return patent


@router.put("/{patent_id}", response_model=PatentOut)
def update_patent(
    patent_id: int,
    patent_data: PatentUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    patent = db.query(Patent).filter(Patent.id == patent_id).first()
    if not patent:
        raise HTTPException(status_code=404, detail="Patent not found")

    for key, value in patent_data.dict(exclude_unset=True).items():
        setattr(patent, key, value)

    db.commit()
    db.refresh(patent)
    return patent


@router.delete("/{patent_id}")
def delete_patent(
    patent_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    patent = db.query(Patent).filter(Patent.id == patent_id).first()
    if not patent:
        raise HTTPException(status_code=404, detail="Patent not found")

    db.delete(patent)
    db.commit()
    return {"message": "Patent deleted successfully"}