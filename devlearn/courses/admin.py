from django.contrib import admin
from .models import Course, Lesson, UserCourseRelation
from embed_video.admin import AdminVideoMixin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

@admin.register(UserCourseRelation)
class UserCourseRelationAdmin(admin.ModelAdmin):
    pass
