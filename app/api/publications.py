from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.api.deps import get_db
from app.models.publication import Publication, PublicationType
from app.schemas.publication import (
    PublicationCreate,
    PublicationUpdate,
    PublicationOut
)
from app.core.auth_guard import get_current_user
from sqlalchemy import func


router = APIRouter()


@router.get("/")
def list_publications(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    year: Optional[int] = None,
    publication_type: Optional[PublicationType] = None,
    search: Optional[str] = None,
):
    query = db.query(Publication)

    if year is not None:
        query = query.filter(Publication.year == year)

    if publication_type is not None:
        query = query.filter(Publication.publication_type == publication_type)

    if search:
        query = query.filter(
            Publication.title.ilike(f"%{search}%")
        )

    total = query.count()

    publications = (
        query
        .order_by(Publication.year.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": publications,
    }




@router.get("/{publication_id}", response_model=PublicationOut)
def get_publication(publication_id: int, db: Session = Depends(get_db)):
    publication = db.query(Publication).filter(Publication.id == publication_id).first()

    if not publication:
        raise HTTPException(status_code=404, detail="Publication not found")

    return publication





@router.post("/", response_model=PublicationOut)
def create_publication(
    publication_data: PublicationCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    publication = Publication(**publication_data.dict())

    db.add(publication)
    db.commit()
    db.refresh(publication)

    return publication





@router.put("/{publication_id}", response_model=PublicationOut)
def update_publication(
    publication_id: int,
    publication_data: PublicationUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    publication = db.query(Publication).filter(Publication.id == publication_id).first()

    if not publication:
        raise HTTPException(status_code=404, detail="Publication not found")

    for key, value in publication_data.dict(exclude_unset=True).items():
        setattr(publication, key, value)

    db.commit()
    db.refresh(publication)

    return publication





@router.delete("/{publication_id}")
def delete_publication(
    publication_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    publication = db.query(Publication).filter(Publication.id == publication_id).first()

    if not publication:
        raise HTTPException(status_code=404, detail="Publication not found")

    db.delete(publication)
    db.commit()

    return {"message": "Publication deleted successfully"}





