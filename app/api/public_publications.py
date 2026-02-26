from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.publication import Publication
from sqlalchemy import desc

router = APIRouter(prefix="/public", tags=["Public"])


@router.get("/publications")
def public_publications(db: Session = Depends(get_db)):
    publications = (
        db.query(Publication)
        .order_by(desc(Publication.year))
        .all()
    )

    return publications