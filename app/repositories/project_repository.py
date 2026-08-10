from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectRepository:
    @staticmethod
    def get_all(db: Session) -> list[Project]:
        return list(db.scalars(select(Project).order_by(Project.completion_year.desc())))

    @staticmethod
    def get_by_id(db: Session, project_id: int) -> Project | None:
        return db.get(Project, project_id)

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> Project | None:
        return db.scalar(select(Project).where(Project.slug == slug))

    @staticmethod
    def create(db: Session, data: ProjectCreate) -> Project:
        project = Project(**data.model_dump())
        db.add(project)
        db.commit()
        db.refresh(project)
        return project

    @staticmethod
    def update(db: Session, project: Project, data: ProjectUpdate) -> Project:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(project, field, value)
        db.commit()
        db.refresh(project)
        return project

    @staticmethod
    def delete(db: Session, project: Project) -> None:
        db.delete(project)
        db.commit()