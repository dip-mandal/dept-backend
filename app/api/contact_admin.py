from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.contact import ContactInfo, ContactMessage
from app.schemas.contact import ContactInfoUpdate, ContactInfoOut, ContactMessageOut
from app.core.auth_guard import get_current_user

router = APIRouter()


@router.get("/", response_model=ContactInfoOut)
def get_contact_info(db: Session = Depends(get_db)):
    return db.query(ContactInfo).first()


@router.put("/", response_model=ContactInfoOut)
def update_contact_info(
    data: ContactInfoUpdate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    info = db.query(ContactInfo).first()

    if not info:
        info = ContactInfo()
        db.add(info)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(info, key, value)

    db.commit()
    db.refresh(info)

    return info


@router.get("/messages")
def list_messages(db: Session = Depends(get_db)):
    return db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()