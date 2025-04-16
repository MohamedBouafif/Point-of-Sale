from enum import Enum
from sqlalchemy import Column , Integer, String, DateTime, Date,func
from ..database import Base
from datetime import datetime, UTC
from app.enums import Gender,  AccountStatus,ContractType
from sqlalchemy.types import Enum as SQLEnum

class Employee(Base):
        __tablename__ = "employee"

        id = Column(Integer, primary_key=True)
        first_name = Column(String, nullable= False)
        last_name = Column(String, nullable= False)
        email = Column(String, nullable= False, unique = True)
        password =Column(String, nullable=True)
        number = Column(Integer, nullable = False)
        birth_date = Column(Date, nullable= True)
        address = Column(Date, nullable=True)
        cnss_number = Column(String,  nullable=True)
        contract_type = Column(SQLEnum(ContractType), nullable=True)
        gender = Column(SQLEnum(Gender), nullable=False)
        Account_status = Column(
                SQLEnum(AccountStatus),
                nullable=False,
                default = AccountStatus.Inactive
        )
        phone_number = Column(String, unique =True, nullable=True)
        created_on = Column(DateTime, nullable=False,  server_default=func.now())

