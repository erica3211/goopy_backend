from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.deps import get_db
from app.schemas.waiting_schema import WaitingCreate, WaitingUpdate, WaitingResponse
from app.services.waiting_service import WaitingService
from app.schemas.common import ApiResponse, PageResponse
from app.core.enums import WaitingStatus
from app.core.response import success

router = APIRouter(prefix="/waitings", tags=["Waitings"])

@router.post("/create", response_model=WaitingResponse)
def create_waiting(dto: WaitingCreate, db: Session = Depends(get_db)):
    service = WaitingService(db)
    waiting = service.create(dto.dict())
    return success(waiting)

@router.get("/list", response_model=ApiResponse[PageResponse[WaitingResponse]])
def get_waitings(
    status: WaitingStatus = Query(..., description="WAITING | IN_PROGRESS | DONE | CANCEL | NO_SHOW"),
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db),
):
    service = WaitingService(db)
    return success(service.paginate_by_status(status, page, size))

@router.get("/{customer_id}", response_model=ApiResponse[WaitingResponse])
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    service = WaitingService(db)
    return success(service.get(customer_id))


@router.put("/{customer_id}", response_model=ApiResponse[WaitingResponse])
def update_customer(
    customer_id: int,
    dto: WaitingUpdate,
    db: Session = Depends(get_db)
):
    service = WaitingService(db)
    return success(service.update(customer_id, dto.dict(exclude_unset=True)))


@router.delete("/{customer_id}", response_model=ApiResponse[None])
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    service = WaitingService(db)
    service.delete(customer_id)
    return success(None, message="삭제 완료")