from django.core.cache import cache
from django.conf import settings


def course_cache_delete():
    get = cache.get('course_cache_query')
    cache.delete(f'course_cache_{get}') # удаляем search_query

    cache.delete(settings.COURSE_CACHE) # удаляем кеш списка курсов
