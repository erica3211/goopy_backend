from pydantic import BaseModel
from datetime import datetime


class AdminCreate(BaseModel):
    id: str
    username: str
    password: str
    role: str  # OWNER / STAFF


class AdminResponse(BaseModel):
    id: str
    username: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True