from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.core.enums import WaitingStatus

class WaitingCreate(BaseModel):
    customer_id: int
    estimated_minutes: int = 15

class WaitingUpdate(BaseModel):
    customer_id: int
    estimated_minutes: int = 15
    status:WaitingStatus
    
class WaitingResponse(BaseModel):
    id: int
    customer_id: int
    name: str
    phone: str
    status: WaitingStatus
    queue_order: int
    slot_id: Optional[int] = None
    estimated_minutes: int
    started_at: Optional[datetime] = None

    class Config:
        from_attributes = True