import uvicorn
from fastapi import FastAPI

from .course.handlers import router as course_router


app = FastAPI()

app.include_router(router=course_router)


@app.get("/")
async def base_rout():
    return {"message": "hello!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
