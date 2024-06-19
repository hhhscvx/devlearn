from django.shortcuts import render, redirect
from .models import Course, UserCourseRelation
from django.core.paginator import Paginator


def test_courses_view(request):
    courses = Course.objects.all()  # Будем проходится по каждому из courses, и в нем по каждому lesson из course.lessons
    paginator = Paginator(courses, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'courses/list.html',
                  {'courses': page_obj})  # page obj сделать?


def course_detail_view(request, slug):
    course = Course.objects.get(slug=slug)
    return render(request,
                  'courses/detail.html',
                  {'course': course})


def user_enroll_to_course_view(request, slug):
    user = request.user
    course = Course.objects.get(slug=slug)
    if user not in course.students.all():
        UserCourseRelation.objects.create(user=user,
                                          course=course,
                                          enrolled=True)
    return redirect('courses:course_detail', course.slug)
