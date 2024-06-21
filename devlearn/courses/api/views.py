from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import LessonSerializer, CourseSerializer, UserLessonRelationSerializer
from ..models import Lesson, Course, UserLessonRelation


from rest_framework.mixins import RetrieveModelMixin


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class UserLessonRelationViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = UserLessonRelation.objects.all()
    permission_class = [IsAuthenticated]
    serializer_class = UserLessonRelationSerializer

    lookup_field = 'lesson'  # так просто /book/<pk>, а щас /book/<book>

    def get_object(self):  # переопределяем метод получения объекта
        obj, created = UserLessonRelation.objects.get_or_create(user=self.request.user,
                                                              lesson_id=self.kwargs['lesson'])  # обращаемся из lookup_field
        print(f'was created: {created}')
        return obj  # получили объект relation, получив айдишник lesson


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
