from django.shortcuts import render, redirect
from .models import Course, UserCourseRelation, Lesson, UserLessonRelation
from django.core.paginator import Paginator


def lesson_completed_view(request, slug):
    lesson = Lesson.objects.get(slug=slug)
    user_lesson = UserLessonRelation.objects.get(user=request.user, lesson=lesson)
    user_lesson.completed = not user_lesson.completed
    return redirect('courses:lesson_detail', slug)


def lesson_detail_view(request, slug):
    lesson = Lesson.objects.get(slug=slug)
    return render(request, 'lessons/detail.html', {'lesson': lesson})


def courses_list_view(request):
    search_query = request.GET.get('search', '')  # по дефолту ''

    if search_query:
        courses = Course.objects.filter(title__icontains=search_query)
    else:
        courses = Course.objects.all()

    paginator = Paginator(courses, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'courses/list.html',
                  {'courses': page_obj})


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
    return redirect('courses:course_detail', slug)
