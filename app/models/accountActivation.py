
from sqlalchemy import Column , Integer, String,DateTime, ForeignKey, Enum,func
from ..database import Base
from app.enums import TokenStatus 
from datetime import datetime, UTC

class AccountActivation(Base):
    __tablename__ = "account_activation"
    id = Column(Integer, primary_key= True)
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable = False)
    email = Column(String, nullable=False)
    token = Column(String, nullable = False)
    status = Column(Enum(TokenStatus), nullable = False)
    created_on = Column(DateTime, nullable=False,  default=datetime.now(UTC))
