from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.project import Project
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:
    @staticmethod
    def list_projects(db: Session) -> list[Project]:
        return ProjectRepository.get_all(db)

    @staticmethod
    def get_project(db: Session, project_id: int) -> Project:
        project = ProjectRepository.get_by_id(db, project_id)
        if not project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        return project

    @staticmethod
    def create_project(db: Session, data: ProjectCreate) -> Project:
        if ProjectRepository.get_by_slug(db, data.slug):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Slug already exists")
        return ProjectRepository.create(db, data)

    @staticmethod
    def update_project(db: Session, project_id: int, data: ProjectUpdate) -> Project:
        project = ProjectService.get_project(db, project_id)
        return ProjectRepository.update(db, project, data)

    @staticmethod
    def delete_project(db: Session, project_id: int) -> None:
        project = ProjectService.get_project(db, project_id)
        ProjectRepository.delete(db, project)