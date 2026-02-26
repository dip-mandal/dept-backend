from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.award import Award

router = APIRouter()


@router.get("/awards")
def public_awards(db: Session = Depends(get_db)):
    awards = (
        db.query(Award)
        .order_by(Award.award_date.desc())
        .all()
    )

    return awards