from celery import shared_task
from celery_singleton import Singleton
from django.db.models import Avg
from django.core.cache import cache
from django.conf import settings
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
