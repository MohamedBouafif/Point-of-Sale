
from sqlalchemy import Column , Integer, Enum
from ..database import Base
from app.enums import RoleType


class EmployeeRole(Base):
    __tablename__ = "employee_roles"
    id = Column(Integer, primary_key=True)
    role = Column(Enum(RoleType))

