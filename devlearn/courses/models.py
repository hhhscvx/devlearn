from django.db import models
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.db.models.signals import post_delete

from .services import fields
from .services.delete_all_cache import course_cache_delete
from .tasks import set_rating
from .receivers import delete_cache_after_course_delete


class Lesson(models.Model):
    course = models.ForeignKey("Course",
                               related_name='lessons',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)

    order = fields.OrderField(blank=True, for_fields='course')
    body = models.TextField(blank=True, null=True)

    video = EmbedVideoField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.course.title}. Урок {self.order}. {self.title}'

    class Meta:
        ordering = ['order']  # сортируем уроки по очереди


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='own_courses',
                              on_delete=models.SET_NULL, null=True)

    students = models.ManyToManyField(User, related_name='courses',
                                      through="UserCourseRelation")

    price = models.IntegerField(default=0)  # discount?????

    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    preview = models.ImageField(upload_to='course_previews/',
                                blank=True, null=True, db_index=True)

    description = models.TextField(max_length=255, blank=True, null=True)

    released = models.DateField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 default=0.00)
    tags = TaggableManager()

    def __str__(self) -> str:
        return f'{self.title} от {self.owner.username}'
    
    class Meta:
        ordering = ['-released']

    def save(self, *args, **kwargs):
        course_cache_delete()

        return super().save(*args, **kwargs)


class UserCourseRelation(models.Model):  # Celery: получить курс и вернуть курс
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # related name?
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    enrolled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)  # "хочу пройти"
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=None,
                                            blank=True, null=True)
    comment = models.TextField(max_length=250, default=None,  # review?
                               blank=True, null=True)

    def __str__(self) -> str:
        return f'Пользователь {self.user.username} поступил на курс {self.course.title}'

    def __init__(self, *args, **kwargs):
        super(UserCourseRelation, self).__init__(*args, **kwargs)
        self.old_rate = self.rate

    def save(self, *args, **kwargs):
        create = not self.pk

        super().save(*args, **kwargs)
        if not (self.rate == self.old_rate) or create:
            course_cache_delete()
            set_rating.delay(self.course.id)


class UserLessonRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)
    like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Пользователь {self.user.username} изучает урок {self.lesson.title}'


# class Comment(models.Model):
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
#                                related_name='comments', null=True, blank=True)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE,
#                                related_name='comments', null=True, blank=True)
#     comment = models.TextField(max_length=250)
#     user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         if self.lesson:
#             return f'{self.user.username} Комментирует урок {self.lesson}: {self.comment}'
#         return f'{self.user.username} Комментирует Курс {self.course}: {self.comment}'

post_delete.connect(delete_cache_after_course_delete, sender=Course)
