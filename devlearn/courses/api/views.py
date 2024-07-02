from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import LessonSerializer, CourseSerializer
from ..models import Lesson, Course
from rest_framework.filters import SearchFilter, OrderingFilter


class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'owner__username']
    ordering_fields = ['title', 'rating', 'price']
