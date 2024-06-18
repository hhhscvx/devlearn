from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('courses/', views.test_courses_view, name='course_list')
]
