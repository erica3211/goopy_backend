from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.deps import get_db
from app.services.customer_service import CustomerService
from app.schemas.customer_schema import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)
from app.schemas.common import ApiResponse, PageResponse
from app.core.response import success

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("", response_model=ApiResponse[CustomerResponse])
def create_customer(dto: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    customer = service.create_customer(dto.dict())
    return success(customer)


@router.get("/by-phone", response_model=ApiResponse[CustomerResponse])
def get_customer_by_phone(
    phone: str = Query(..., description="전화번호"),
    db: Session = Depends(get_db),
):
    service = CustomerService(db)
    return success(service.get_by_phone(phone))


@router.get("", response_model=ApiResponse[PageResponse[CustomerResponse]])
def get_all_customers(
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    service = CustomerService(db)
    return success(service.paginate(page, size))


@router.put("/{customer_id}", response_model=ApiResponse[CustomerResponse])
def update_customer(
    customer_id: int,
    dto: CustomerUpdate,
    db: Session = Depends(get_db)
):
    service = CustomerService(db)
    return success(service.update(customer_id, dto.dict(exclude_unset=True)))


@router.delete("/{customer_id}", response_model=ApiResponse[None])
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    service.delete(customer_id)
    return success(None, message="삭제 완료")