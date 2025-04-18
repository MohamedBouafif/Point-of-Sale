from pydantic import BaseModel
from datetime import date,datetime
from app.enums import ContractType, Gender, AccountStatus

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class EmployeeBase(OurBaseModel):
    first_name :str
    last_name   :str
    email : str
    number :int
    birth_date : date |None = None
    address : str |None = None
    cnss_number :str |None =  None
    contract_type : ContractType|None  = None
    gender :Gender
    phone_number:str|None = None 
    
class EmployeeCreate(EmployeeBase):
    password :str |None =  None

    

class EmployeeOut(EmployeeBase):
    id : int
    created_on : datetime