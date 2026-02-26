from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.gallery import Gallery

router = APIRouter()


@router.get("/gallery")
def public_gallery(db: Session = Depends(get_db)):
    return (
        db.query(Gallery)
        .order_by(Gallery.created_at.desc())
        .all()
    )