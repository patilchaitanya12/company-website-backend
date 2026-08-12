from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.service import Service
from app.repositories.service_repository import ServiceRepository
from app.schemas.service import ServiceCreate, ServiceUpdate


class ServiceService:
    @staticmethod
    def list_services(db: Session) -> list[Service]:
        return ServiceRepository.get_all(db)

    @staticmethod
    def get_service(db: Session, service_id: int) -> Service:
        service = ServiceRepository.get_by_id(db, service_id)
        if not service:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
        return service

    @staticmethod
    def create_service(db: Session, data: ServiceCreate) -> Service:
        return ServiceRepository.create(db, data)

    @staticmethod
    def update_service(db: Session, service_id: int, data: ServiceUpdate) -> Service:
        service = ServiceService.get_service(db, service_id)
        return ServiceRepository.update(db, service, data)

    @staticmethod
    def delete_service(db: Session, service_id: int) -> None:
        service = ServiceService.get_service(db, service_id)
        ServiceRepository.delete(db, service)