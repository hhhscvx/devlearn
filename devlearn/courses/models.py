from django.db import models
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

from .services import fields


class Lesson(models.Model):
    course = models.ForeignKey("Course",
                               related_name='lessons',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)

    order = fields.OrderField(blank=True, for_fields='course')
    body = models.TextField(blank=True, null=True)
    # completed = models.BooleanField(default=False)

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

    price = models.IntegerField(default=0)

    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)
    preview = models.ImageField(upload_to='course_previews/',
                                blank=True, null=True, db_index=True)
    # completed = models.BooleanField(default=False)

    description = models.TextField(max_length=255, blank=True, null=True)

    released = models.DateField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 default=None, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return f'{self.title} от {self.owner.username}'


class UserCourseRelation(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    enrolled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)  # "хочу пройти"
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=None,
                                            blank=True, null=True)
    comment = models.TextField(max_length=250, default=None,
                               blank=True, null=True)

    def __str__(self) -> str:
        return f'Пользователь {self.user.username} поступил на курс {self.course.title}'

# мб нужны будут черновики курса? Его же не за один присест создают...
