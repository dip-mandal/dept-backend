from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.contact import ContactInfo, ContactMessage
from app.schemas.contact import ContactMessageCreate
from app.utils.email import send_contact_email

router = APIRouter()


@router.get("/contact")
def public_contact_info(db: Session = Depends(get_db)):
    return db.query(ContactInfo).first()


@router.post("/contact")
def send_contact_message(
    data: ContactMessageCreate,
    db: Session = Depends(get_db)
):
    message = ContactMessage(**data.dict())
    db.add(message)
    db.commit()

    send_contact_email(
        data.name,
        data.email,
        data.subject,
        data.message
    )

    return {"message": "Message sent successfully"}