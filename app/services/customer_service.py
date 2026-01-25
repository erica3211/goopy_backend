from fastapi import HTTPException
from app.services.base_service import BaseService
from app.models.customer_model import Customer

class CustomerService(BaseService):
    model = Customer
    

    # 고객만의 규칙은 여기서 추가
    def create_customer(self, obj_in: dict):
        if self.db.query(Customer).filter(Customer.phone == obj_in["phone"]).first():
            raise ValueError("이미 등록된 전화번호입니다.")
        return self.create(obj_in)
    
    def get_by_phone(self, phone: str):
        customer = (
            self.db.query(Customer)
            .filter(Customer.phone == phone)
            .first()
        )

        if not customer:
            raise HTTPException(status_code=404, detail="고객이 존재하지 않습니다")

        return customer