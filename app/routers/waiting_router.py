from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.deps import get_db
from app.schemas.waiting_schema import WaitingCreate, WaitingUpdate, WaitingResponse
from app.services.waiting_service import WaitingService
from app.schemas.common import ApiResponse, PageResponse
from app.core.enums import WaitingStatus
from app.core.response import success

router = APIRouter(tags=["Waitings"])

@router.post("/create_waiting",response_model=ApiResponse[WaitingResponse])
def create_waiting(
    customer_id: int,
    estimated_minutes: int,
    db: Session = Depends(get_db),
):
    service = WaitingService(db)
    service.create_waiting(
        customer_id=customer_id,
        estimated_minutes=estimated_minutes,
    )
    return success()

@router.get("/get_waiting_list", response_model=ApiResponse[PageResponse[WaitingResponse]])
def get_waitings(
    status: WaitingStatus = Query(..., description="WAITING | IN_PROGRESS | DONE | CANCEL | NO_SHOW"),
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db),
):
    service = WaitingService(db)
    return success(service.paginate_by_status(status, page, size))

@router.get("/get_waiting/{customer_id}", response_model=ApiResponse[WaitingResponse])
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    service = WaitingService(db)
    return success(service.get(customer_id))


@router.put("/update_waiting/{waiting_id}", response_model=ApiResponse[WaitingUpdate])
def update_customer(
    waiting_id: int,
    status : WaitingStatus,
    estimated_minutes : int | None = None,
    db: Session = Depends(get_db)
):
    service = WaitingService(db)
    return success(service.update_waiting(waiting_id=waiting_id, estimated_minutes=estimated_minutes, status=status))


@router.delete("/delete_waiting/{customer_id}", response_model=ApiResponse[None])
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    service = WaitingService(db)
    service.delete(customer_id)
    return success(None, message="삭제 완료")