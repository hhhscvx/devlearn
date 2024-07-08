from django.urls import path
from . import views

app_name = 'learner'

urlpatterns = [
    path('profile/<slug:username>/', views.profile_view, name='profile')
]
