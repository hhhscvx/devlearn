from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('account/login/', views.CustomLoginView.as_view(), name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register/', views.register_view, name='register'),
    path('learn/', views.my_courses_view, name='my_course_list')
]
