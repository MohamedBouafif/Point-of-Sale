from sqlalchemy.orm import Session
from .. import models,schemas

def get_user(db:Session, id : int):
    return db.query(models.Employee).filter(models.Employee.id ==id ).first()

def get_by_email(db:Session , email:str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def get_all(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def add(db:Session, employee:schemas.EmployeeCreate):
    #fix me later 
    password = employee.password 
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return schemas.EmployeeOut(**db_employee.__dict__)