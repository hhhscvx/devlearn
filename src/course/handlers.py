from fastapi import APIRouter


router = APIRouter(prefix="/course", tags=["Course"])



@router.get("/{course_id}")
async def get_course(course_id: int):
    return {'id': course_id, 'title': 'FastAPI TOP COURSE'}

