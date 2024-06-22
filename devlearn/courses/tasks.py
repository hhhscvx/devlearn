from celery import shared_task
from celery_singleton import Singleton
from django.db.models import Avg
import time


@shared_task(base=Singleton)
def set_rating(course_id):
    from .models import Course, UserCourseRelation

    time.sleep(5)

    course = Course.objects.get(id=course_id)
    rating = UserCourseRelation.objects.filter(course=course).aggregate(rating=Avg('rate')).get('rating')
    if rating:
        course.rating = rating
    else:
        course.rating = 0.0
    course.save()
