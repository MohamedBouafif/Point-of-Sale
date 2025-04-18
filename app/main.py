from fastapi import FastAPI,Depends, HTTPException
import uvicorn
from app import schemas
from sqlalchemy.orm  import Session
from app.routers import crud
from .database import SessionLocal, engine
app = FastAPI()


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/employee/", response_model = schemas.EmployeeOut ) 
def create_employee(employee: schemas.EmployeeCreate, db :Session = Depends(get_db)):
    db_employee = crud.get_by_email(db, email = employee.email)
    if db_employee:
        raise HTTPException(status_code = 400, detail = "Email already registered")
    return crud.add(db=db , employee=employee)





#for debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)