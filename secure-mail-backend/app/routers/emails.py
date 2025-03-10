from fastapi import APIRouter, Depends, HTTPException
from models import Email, User
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import get_db

router = APIRouter()

class EmailCreate(BaseModel):
    sender_id: int
    recipient_email: str
    encrypted_subject: str
    encrypted_body: str

@router.post("/")
def send_email(email: EmailCreate, db: Session = Depends(get_db)):
    recipient = db.query(User).filter(User.email == email.recipient_email).first()
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")

    db_email = Email(
        sender_id=email.sender_id,
        recipient_id=recipient.id,
        encrypted_subject=email.encrypted_subject,
        encrypted_body=email.encrypted_body
    )
    db.add(db_email)
    db.commit()
    return {"msg": "Email sent!"}

@router.get("/{user_id}")
def get_inbox(user_id: int, db: Session = Depends(get_db)):
    emails = db.query(Email).filter(Email.recipient_id==user_id).all()
    return emails
