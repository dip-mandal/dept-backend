from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.book import Book

router = APIRouter()


@router.get("/books")
def public_books(db: Session = Depends(get_db)):
    books = (
        db.query(Book)
        .order_by(Book.year.desc())
        .all()
    )

    return books