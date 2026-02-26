from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.faculty import Faculty
from app.schemas.faculty import FacultyUpdate, FacultyOut
from app.core.auth_guard import get_current_user

router = APIRouter()


@router.get("/", response_model=FacultyOut)
def get_faculty(db: Session = Depends(get_db)):
    faculty = db.query(Faculty).first()
    if not faculty:
        raise HTTPException(status_code=404, detail="Faculty not found")
    return faculty


@router.put("/", response_model=FacultyOut)
def update_faculty(
    faculty_data: FacultyUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    faculty = db.query(Faculty).first()

    if not faculty:
        faculty = Faculty(**faculty_data.dict())
        db.add(faculty)
    else:
        for key, value in faculty_data.dict(exclude_unset=True).items():
            setattr(faculty, key, value)

    db.commit()
    db.refresh(faculty)

    return faculty