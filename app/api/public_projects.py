# app/api/public_projects.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.project import Project

router = APIRouter()

@router.get("/projects")
def public_projects(db: Session = Depends(get_db)):
    return db.query(Project).order_by(Project.id.desc()).all()