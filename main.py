from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}@app.get("/")
@app.get("/raouf")
async def root():
    return {"message": "we World"}