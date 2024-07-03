from django.core.cache import cache
from django.conf import settings


def cache_delete(cache_get=None, delete_get=None, to_delete=None):
    if cache_get:
        get = cache.get(cache_get) # lesson_detail_slug_cache
        cache.delete(f'{delete_get}{get}') # lesson_detail_{slug}
    if to_delete:
        cache.delete(to_delete)
    


def course_cache_delete():
    cache_delete(cache_get='course_cache_query', delete_get='course_cache_', to_delete=settings.COURSE_CACHE)


def course_detail_cache_delete():
    cache_delete(cache_get='course_detail_slug_cache', delete_get='course_detail_', to_delete='course_detail_slug_cache')

def lesson_detail_cache_delete():
    cache_delete(cache_get='lesson_detail_slug_cache', delete_get='lesson_detail_', to_delete='lesson_detail_slug_cache')

def user_lesson_completed_cache_delete():
    cache_delete(cache_get='lesson_detail_slug_cache', delete_get='user_lesson_completed_cache_', to_delete='lesson_detail_slug_cache')
