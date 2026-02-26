from sqlalchemy.orm import Session
from app.models.award import Award
from app.schemas.award import AwardCreate, AwardUpdate


def create_award(db: Session, award: AwardCreate, faculty_id: int):
    db_award = Award(**award.dict(), faculty_id=faculty_id)
    db.add(db_award)
    db.commit()
    db.refresh(db_award)
    return db_award


def get_awards(db: Session, skip: int = 0, limit: int = 10, search: str | None = None):
    query = db.query(Award)

    if search:
        query = query.filter(Award.title.ilike(f"%{search}%"))

    total = query.count()
    awards = query.offset(skip).limit(limit).all()

    return total, awards


def get_award(db: Session, award_id: int):
    return db.query(Award).filter(Award.id == award_id).first()


def update_award(db: Session, award_id: int, award: AwardUpdate):
    db_award = get_award(db, award_id)
    if not db_award:
        return None

    for key, value in award.dict().items():
        setattr(db_award, key, value)

    db.commit()
    db.refresh(db_award)
    return db_award


def delete_award(db: Session, award_id: int):
    db_award = get_award(db, award_id)
    if not db_award:
        return None

    db.delete(db_award)
    db.commit()
    return db_award