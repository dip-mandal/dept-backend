from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from app.api.deps import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.core.auth_guard import get_current_user

router = APIRouter()



@router.get("/")
def list_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    category: Optional[str] = None,
):
    query = db.query(Book)

    if category:
        query = query.filter(Book.category == category)

    total = query.with_entities(func.count()).scalar()

    books = (
        query.order_by(Book.year.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": books,
    }




@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book





@router.post("/", response_model=BookOut)
def create_book(
    book_data: BookCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    book = Book(**book_data.dict())

    db.add(book)
    db.commit()
    db.refresh(book)

    return book




@router.put("/{book_id}", response_model=BookOut)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)

    return book



@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}




