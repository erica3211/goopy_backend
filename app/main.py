from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine
from .models import Base, User
from .deps import get_db

app = FastAPI()

# 테이블 생성
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL 연결 성공 🎉"}

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user