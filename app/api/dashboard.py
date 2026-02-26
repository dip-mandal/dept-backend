from app.models.patent import Patent
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.api.deps import get_db
from app.models.publication import Publication
from app.models.project import Project
from app.models.book import Book
from app.models.phd_student import PhDStudent
from app.core.auth_guard import get_current_user
from app.models.award import Award


router = APIRouter()



@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    total_publications = db.query(func.count(Publication.id)).scalar()
    total_projects = db.query(func.count(Project.id)).scalar()
    total_books = db.query(func.count(Book.id)).scalar()
    total_phd_students = db.query(func.count(PhDStudent.id)).scalar()
    total_patents = db.query(func.count(Patent.id)).scalar()
    total_awards = db.query(func.count(Award.id)).scalar()

    total_completed_phd = db.query(func.count(PhDStudent.id)) \
        .filter(PhDStudent.status == "completed") \
        .scalar()

    total_ongoing_phd = db.query(func.count(PhDStudent.id)) \
        .filter(PhDStudent.status == "ongoing") \
        .scalar()

    total_funding_amount = db.query(func.sum(Project.amount)).scalar() or 0

    return {
        "total_publications": total_publications,
        "total_projects": total_projects,
        "total_books": total_books,
        "total_phd_students": total_phd_students,
        "total_patents": total_patents,
        "total_awards": total_awards,
        "total_completed_phd": total_completed_phd,
        "total_ongoing_phd": total_ongoing_phd,
        "total_funding_amount": total_funding_amount,
    }
    
    
    
    


@router.get("/publications-by-year")
def publications_by_year(db: Session = Depends(get_db)):
    results = (
        db.query(
            Publication.year,
            func.count(Publication.id)
        )
        .group_by(Publication.year)
        .order_by(Publication.year)
        .all()
    )

    return [
        {
            "year": year,
            "count": count
        }
        for year, count in results
    ]
    
    
    

@router.get("/funding-by-agency")
def funding_by_agency(db: Session = Depends(get_db)):
    results = (
        db.query(
            Project.funding_agency,
            func.sum(Project.amount)
        )
        .group_by(Project.funding_agency)
        .all()
    )

    return [
        {
            "funding_agency": agency,
            "total_amount": total or 0
        }
        for agency, total in results
    ]
    
    


@router.get("/patents-by-status")
def patents_by_status(db: Session = Depends(get_db)):
    data = (
        db.query(Patent.status, func.count(Patent.id))
        .group_by(Patent.status)
        .all()
    )

    return [
        {"status": row[0], "count": row[1]}
        for row in data
    ]


    