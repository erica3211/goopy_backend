from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.admin_schema import AdminCreate, AdminResponse
from app.services.admin_service import create_admin

router = APIRouter(
    prefix="/admins",
    tags=["Admins"]
)


@router.post("", response_model=AdminResponse)
def create(dto: AdminCreate, db: Session = Depends(get_db)):
    return create_admin(db, dto)