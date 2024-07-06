from decimal import Decimal
from celery import shared_task
from celery_singleton import Singleton
from django.db.models import Avg
from django.contrib.auth.models import User
from .services.delete_all_cache import course_cache_delete


@shared_task(base=Singleton)
def set_rating(course_id):
    from .models import Course, UserCourseRelation

    course = Course.objects.get(id=course_id)
    rating = UserCourseRelation.objects.filter(course=course).aggregate(rating=Avg('rate')).get('rating')
    if rating:
        course.rating = rating
    else:
        course.rating = 0.0
    course.save()
    course_cache_delete()


@shared_task(base=Singleton)
def set_completed_percent(course_id, request_user_id: int):
    try:
        from .models import UserCourseRelation, UserLessonRelation
        user_lesson: UserLessonRelation = UserLessonRelation.objects.filter(
            completed=True, lesson__course_id=course_id, user_id=request_user_id)
        all_lessons_count = len(UserLessonRelation.objects.filter(lesson__course_id=course_id, user_id=request_user_id))
        completed_percent = round(Decimal((len(user_lesson) / all_lessons_count) * 100), 2)

        user_course = UserCourseRelation.objects.get(user_id=request_user_id, course_id=course_id)
        user_course.completed_percent = completed_percent
        if completed_percent == 100:
            user_course.completed = True
        user_course.save()
    except Exception as e:
        print(f"Ошибка в таске: {e}")
