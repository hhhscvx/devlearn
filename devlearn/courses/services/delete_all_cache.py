from django.core.cache import cache
from django.conf import settings


def course_cache_delete():
    cache.delete(settings.COURSE_CACHE)
    course_cache_query = cache.get('course_cache_query')
    cache.delete(f'course_cache_{course_cache_query}')
