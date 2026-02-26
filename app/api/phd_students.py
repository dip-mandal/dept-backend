from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from app.api.deps import get_db
from app.models.phd_student import PhDStudent
from app.schemas.phd_student import (
    PhDStudentCreate,
    PhDStudentUpdate,
    PhDStudentOut
)
from app.core.auth_guard import get_current_user

router = APIRouter()




@router.get("/")
def list_phd_students(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = None,
):
    query = db.query(PhDStudent)

    if status:
        query = query.filter(PhDStudent.status == status)

    total = query.with_entities(func.count()).scalar()

    students = (
        query.order_by(PhDStudent.award_date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": students,
    }




@router.get("/{student_id}", response_model=PhDStudentOut)
def get_phd_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(PhDStudent).filter(PhDStudent.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student





@router.post("/", response_model=PhDStudentOut)
def create_phd_student(
    student_data: PhDStudentCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    student = PhDStudent(**student_data.dict())

    db.add(student)
    db.commit()
    db.refresh(student)

    return student




@router.put("/{student_id}", response_model=PhDStudentOut)
def update_phd_student(
    student_id: int,
    student_data: PhDStudentUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    student = db.query(PhDStudent).filter(PhDStudent.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student_data.dict(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student





@router.delete("/{student_id}")
def delete_phd_student(
    student_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    student = db.query(PhDStudent).filter(PhDStudent.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}






