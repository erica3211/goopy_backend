from sqlalchemy.orm import Session
from app.models.admin_model import Admin
from app.schemas.admin_schema import AdminCreate


def create_admin(db: Session, dto: AdminCreate):
    admin = Admin(
        id=dto.id,
        username=dto.username,
        password=dto.password,  # ⚠️ 나중에 해시 처리
        role=dto.role,
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin