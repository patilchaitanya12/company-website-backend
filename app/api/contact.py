from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_admin
from app.database.session import get_db
from app.models.admin import AdminUser
from app.schemas.contact import ContactCreate, ContactOut
from app.services.contact_service import ContactService

router = APIRouter(prefix="/contact", tags=["contact"])


@router.post("", response_model=ContactOut, status_code=201)
def submit_contact(data: ContactCreate, db: Session = Depends(get_db)):
    return ContactService.create_request(db, data)


@router.get("", response_model=list[ContactOut])
def list_contacts(
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin),
):
    return ContactService.list_requests(db)