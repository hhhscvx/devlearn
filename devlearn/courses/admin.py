from django.contrib import admin
from .models import Course, Lesson, UserCourseRelation, UserLessonRelation, LessonComment, Review
from embed_video.admin import AdminVideoMixin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lesson)
class LessonAdmin(AdminVideoMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(UserCourseRelation)
class UserCourseRelationAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrolled', 'like', 'in_bookmarks']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review', 'rate', 'created', 'updated']

@admin.register(UserLessonRelation)
class UserLessonRelationAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed', 'like']

@admin.register(LessonComment)
class LessonCommentAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'user', 'comment', 'created']
