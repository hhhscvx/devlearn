from django.contrib import admin
from .models import Course, Lesson, UserCourseRelation
from embed_video.admin import AdminVideoMixin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lesson)
class LessonAdmin(AdminVideoMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(UserCourseRelation)
class UserCourseRelationAdmin(admin.ModelAdmin):
    pass
