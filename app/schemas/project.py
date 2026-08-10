from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProjectImageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_url: str


class ProjectBase(BaseModel):
    title: str
    slug: str
    description: str
    industry: str
    completion_year: int


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    title: str | None = None
    slug: str | None = None
    description: str | None = None
    industry: str | None = None
    completion_year: int | None = None


class ProjectOut(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    images: list[ProjectImageOut] = []


class ProjectListOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    slug: str
    industry: str
    completion_year: int