from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.contact import ContactRequest
from app.schemas.contact import ContactCreate


class ContactRepository:
    @staticmethod
    def get_all(db: Session) -> list[ContactRequest]:
        return list(
            db.scalars(select(ContactRequest).order_by(ContactRequest.created_at.desc()))
        )

    @staticmethod
    def create(db: Session, data: ContactCreate) -> ContactRequest:
        contact = ContactRequest(**data.model_dump())
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact