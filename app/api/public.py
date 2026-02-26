from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.api.deps import get_db
from app.models.faculty import Faculty
from app.models.publication import Publication
from app.models.project import Project
from app.models.patent import Patent
from app.models.phd_student import PhDStudent

router = APIRouter(prefix="/public", tags=["Public"])


@router.get("/faculty")
def get_faculty_profile(db: Session = Depends(get_db)):
    faculty = db.query(Faculty).first()

    if not faculty:
        return None

    total_publications = db.query(func.count(Publication.id)).scalar()
    total_projects = db.query(func.count(Project.id)).scalar()
    total_patents = db.query(func.count(Patent.id)).scalar()
    total_phd = db.query(func.count(PhDStudent.id)).scalar()
    total_funding = db.query(func.sum(Project.amount)).scalar() or 0

    return {
        "profile": faculty,
        "metrics": {
            "publications": total_publications,
            "projects": total_projects,
            "patents": total_patents,
            "phd_students": total_phd,
            "funding": total_funding,
        },
    }