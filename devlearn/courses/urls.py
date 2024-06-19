from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'courses'

urlpatterns = [
    path('courses/', views.test_courses_view, name='course_list'),
    path('course/<slug:slug>', views.course_detail_view, name='course_detail'),
    path('course/<slug:slug>/enroll', views.user_enroll_to_course_view, name='course_enroll'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
