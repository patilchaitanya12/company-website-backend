from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_admin
from app.database.session import get_db
from app.models.admin import AdminUser
from app.schemas.service import ServiceCreate, ServiceOut, ServiceUpdate
from app.services.service_service import ServiceService

router = APIRouter(prefix="/services", tags=["services"])


@router.get("", response_model=list[ServiceOut])
def list_services(db: Session = Depends(get_db)):
    return ServiceService.list_services(db)


@router.get("/{service_id}", response_model=ServiceOut)
def get_service(service_id: int, db: Session = Depends(get_db)):
    return ServiceService.get_service(db, service_id)


@router.post("", response_model=ServiceOut, status_code=201)
def create_service(
    data: ServiceCreate,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin),
):
    return ServiceService.create_service(db, data)


@router.put("/{service_id}", response_model=ServiceOut)
def update_service(
    service_id: int,
    data: ServiceUpdate,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin),
):
    return ServiceService.update_service(db, service_id, data)


@router.delete("/{service_id}", status_code=204)
def delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    _: AdminUser = Depends(get_current_admin),
):
    ServiceService.delete_service(db, service_id)