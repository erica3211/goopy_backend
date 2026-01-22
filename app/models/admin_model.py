from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime
from app.database import Base


class Admin(Base):
    __tablename__ = "admin"

    id = Column(String(50), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    role = Column(String(20), nullable=False)  # OWNER / STAFF
    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)