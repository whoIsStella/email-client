from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Email, User

router = APIRouter()


class EmailCreate(BaseModel):
    sender_id: int
    recipient_email: str
    encrypted_subject: str
    encrypted_body: str


@router.post("/", status_code=201)
def send_email(email: EmailCreate, db: Session = Depends(get_db)):
    recipient = db.query(User).filter(User.email == email.recipient_email).first()
    if recipient is None:
        raise HTTPException(status_code=404, detail="Recipient not found")

    db_email = Email(
        sender_id=email.sender_id,
        recipient_id=recipient.id,
        encrypted_subject=email.encrypted_subject,
        encrypted_body=email.encrypted_body,
    )
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return {"id": db_email.id}


@router.get("/{user_id}")
def get_inbox(user_id: int, db: Session = Depends(get_db)):
    rows = db.query(Email).filter(Email.recipient_id == user_id).all()
    return [
        {
            "id": row.id,
            "sender_id": row.sender_id,
            "recipient_id": row.recipient_id,
            "encrypted_subject": row.encrypted_subject,
            "encrypted_body": row.encrypted_body,
        }
        for row in rows
    ]
