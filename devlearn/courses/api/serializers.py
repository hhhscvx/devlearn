from rest_framework import serializers
from ..models import Lesson, Course, UserLessonRelation, UserCourseRelation


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserLessonRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLessonRelation
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class UserCourseRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseRelation
        fields = '__all__'
