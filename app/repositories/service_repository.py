from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.service import Service
from app.schemas.service import ServiceCreate, ServiceUpdate


class ServiceRepository:
    @staticmethod
    def get_all(db: Session) -> list[Service]:
        return list(db.scalars(select(Service).order_by(Service.id)))

    @staticmethod
    def get_by_id(db: Session, service_id: int) -> Service | None:
        return db.get(Service, service_id)

    @staticmethod
    def create(db: Session, data: ServiceCreate) -> Service:
        service = Service(**data.model_dump())
        db.add(service)
        db.commit()
        db.refresh(service)
        return service

    @staticmethod
    def update(db: Session, service: Service, data: ServiceUpdate) -> Service:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(service, field, value)
        db.commit()
        db.refresh(service)
        return service

    @staticmethod
    def delete(db: Session, service: Service) -> None:
        db.delete(service)
        db.commit()