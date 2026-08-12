from sqlalchemy.orm import Session

from app.models.contact import ContactRequest
from app.repositories.contact_repository import ContactRepository
from app.schemas.contact import ContactCreate


class ContactService:
    @staticmethod
    def list_requests(db: Session) -> list[ContactRequest]:
        return ContactRepository.get_all(db)

    @staticmethod
    def create_request(db: Session, data: ContactCreate) -> ContactRequest:
        return ContactRepository.create(db, data)