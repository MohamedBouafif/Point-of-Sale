from sqlalchemy.orm import Session
from .. import models,schemas
import emailUtil
def get_user(db:Session, id : int):
    return db.query(models.Employee).filter(models.Employee.id ==id ).first()

def get_by_email(db:Session , email:str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def get_all(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

async def add(db:Session, employee:schemas.EmployeeCreate):
    #fix me later 
    employee.password = employee.password + "fake hash"
    employee_data =employee.model_dump()
    employee_data.pop('confirm_password')
    roles = employee_data.pop('roles')
    db_employee = models.Employee()
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    for role in roles:
        db_role = models.EmployeeRole(role = role, employee_id = db_employee.id)
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
    
    await emailUtil.simple_send([employee.email])
    return schemas.EmployeeOut(**db_employee.__dict__)