from django.db.models.signals import post_delete
from django.dispatch import receiver
from .services.delete_all_cache import course_cache_delete


@receiver(post_delete, sender=None)
def delete_course_cache_after_course_delete(*args, **kwargs):
    course_cache_delete()
