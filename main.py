import uvicorn
from fastapi import FastAPI


app = FastAPI()



@app.get("/")
async def base_rout():
    return {"message": "hello!"}



if __name__ == "__main__":
    uvicorn.run("main:app")
