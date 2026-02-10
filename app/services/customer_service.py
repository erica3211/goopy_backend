from app.services.base_service import BaseService
from app.models.customer_model import Customer

class CustomerService(BaseService):
    model = Customer
    

    # 고객만의 규칙은 여기서 추가
    def create_customer(self, name: str, phone: str):
        if self.db.query(Customer).filter(Customer.phone == phone).first():
            raise ValueError("이미 등록된 전화번호입니다.")

        customer = Customer(name=name, phone=phone)
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)
        return customer
        
    def get_by_phone(self, phone: str):
        return (
        self.db.query(Customer)
        .filter(Customer.phone == phone)
        .first()
    )