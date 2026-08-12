from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class ContactCreate(BaseModel):
    name: str
    company: str
    email: EmailStr
    phone: str
    requirement: str


class ContactOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    company: str
    email: str
    phone: str
    requirement: str
    created_at: datetime