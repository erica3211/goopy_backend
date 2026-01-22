from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:990704@localhost:5432/goopy"

engine = create_engine(
    DATABASE_URL,
    echo=True  # SQL 로그 보고 싶으면 True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ✅ 이게 빠져 있어서 에러 난 거임
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()