from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'courses'

urlpatterns = [
    path('courses/', views.courses_list_view, name='course_list'),
    path('course/<slug:slug>/', views.course_detail_view, name='course_detail'),
    path('course/<slug:slug>/enroll/', views.user_enroll_to_course_view, name='course_enroll'),
    path('course/<int:course_id>/set-review/', views.set_course_review, name='set_course_review'),
    path('course/<int:course_id>/reviews/', views.course_review_list, name='course_review_list'),

    path('lesson/<slug:slug>/', views.lesson_detail_view, name='lesson_detail'),
    path('lesson/<slug:slug>/complete', views.lesson_completed_view, name='lesson_completed'),
    path('lesson/<slug:slug>/comment/delete/<int:pk>', views.lesson_comment_delete_view, name='comment_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
