from pydantic import BaseModel, ConfigDict


class ServiceBase(BaseModel):
    title: str
    description: str
    icon: str


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    icon: str | None = None


class ServiceOut(ServiceBase):
    model_config = ConfigDict(from_attributes=True)

    id: int