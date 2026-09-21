from sqlalchemy import Column, ForeignKey, Integer, String, Text

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    public_key = Column(Text, nullable=False)


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recipient_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    encrypted_subject = Column(Text, nullable=False)
    encrypted_body = Column(Text, nullable=False)
