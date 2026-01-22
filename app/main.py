from fastapi import FastAPI
from app.database import engine
from app.models import customer_model, visit_model, stylist_slot_model
from app.routers.customer_router import router as customer_router
from app.routers.visit_router import router as visit_router
from app.routers.admin_router import router as admin_router
from app.database import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(customer_router)
app.include_router(visit_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"message": "GOOPY FastAPI 서버 실행 중 🚀"}