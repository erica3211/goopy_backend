from fastapi import FastAPI, HTTPException
from app.core.exceptions import http_exception_handler
from app.database import engine
from app.models import customer_model, stylist_slot_model, waiting_model
from app.routers.customer_router import router as customer_router
from app.routers.waiting_router import router as waiting_router
from app.routers.admin_router import router as admin_router
from app.database import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_exception_handler(HTTPException, http_exception_handler)

Base.metadata.create_all(bind=engine)

app.include_router(customer_router)
app.include_router(waiting_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"message": "GOOPY FastAPI 서버 실행 중 🚀"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # 프론트 주소
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)