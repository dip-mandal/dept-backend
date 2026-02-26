from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.patent import Patent

router = APIRouter()


@router.get("/patents")
def public_patents(db: Session = Depends(get_db)):
    """
    Public endpoint to fetch all patents
    Ordered by newest first
    """
    patents = (
        db.query(Patent)
        .order_by(Patent.id.desc())
        .all()
    )

    return patents