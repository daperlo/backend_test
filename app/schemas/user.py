from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    role: str  # admin / user


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True