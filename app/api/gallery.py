from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from app.api.deps import get_db
from app.models.gallery import Gallery
from app.schemas.gallery import GalleryCreate, GalleryUpdate, GalleryOut
from app.core.auth_guard import get_current_user

router = APIRouter()


@router.get("/")
def list_gallery(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 20,
):
    query = db.query(Gallery)
    total = query.with_entities(func.count()).scalar()

    items = (
        query.order_by(Gallery.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": items,
    }


@router.post("/", response_model=GalleryOut)
def create_gallery(
    data: GalleryCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    item = Gallery(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{item_id}", response_model=GalleryOut)
def update_gallery(
    item_id: int,
    data: GalleryUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    item = db.query(Gallery).filter(Gallery.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}")
def delete_gallery(
    item_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    item = db.query(Gallery).filter(Gallery.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404)

    db.delete(item)
    db.commit()
    return {"message": "Deleted"}