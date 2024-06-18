from django.shortcuts import render
from .models import Course, Lesson, UserCourseRelation


def test_courses_view(request):
    courses = Course.objects.all()  # Будем проходится по каждому из courses, и в нем по каждому lesson из course.lessons
    return render(request,
                  'courses/list.html',
                  {'courses': courses})
