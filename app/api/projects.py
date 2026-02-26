from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from app.api.deps import get_db
from app.models.project import Project
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectOut
)
from app.core.auth_guard import get_current_user

router = APIRouter()


@router.get("/")
def list_projects(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    status: Optional[str] = None,
    funding_agency: Optional[str] = None,
    role: Optional[str] = None,
):
    query = db.query(Project)

    if status:
        query = query.filter(Project.status == status)

    if funding_agency:
        query = query.filter(Project.funding_agency.ilike(f"%{funding_agency}%"))

    if role:
        query = query.filter(Project.role == role)

    total = query.with_entities(func.count()).scalar()

    projects = (
        query.order_by(Project.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": projects,
    }





@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project










@router.post("/", response_model=ProjectOut)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    project = Project(**project_data.dict())

    db.add(project)
    db.commit()
    db.refresh(project)

    return project








@router.put("/{project_id}", response_model=ProjectOut)
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in project_data.dict(exclude_unset=True).items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project










@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}













