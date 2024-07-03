from django.shortcuts import render, redirect
from .models import Course, UserCourseRelation, Lesson, UserLessonRelation, LessonComment
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.contrib.auth.models import User
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .services.delete_all_cache import lesson_detail_cache_delete
from django.http import HttpRequest, HttpResponse


def lesson_comment_delete_view(request: HttpRequest, slug, pk):
    comment = LessonComment.objects.get(pk=pk)
    comment.delete()
    return redirect('courses:lesson_detail', slug)


def lesson_completed_view(request: HttpRequest, slug):
    lesson = Lesson.objects.get(slug=slug)
    user_lesson, _ = UserLessonRelation.objects.get_or_create(user=request.user, lesson=lesson)
    user_lesson.completed = True
    user_lesson.save()
    return redirect('courses:lesson_detail', slug)


@login_required
def lesson_detail_view(request: HttpRequest, slug):
    lesson_cache_key = f'lesson_cache_{slug}'
    lesson = cache.get(lesson_cache_key)
    if not lesson:
        lesson = Lesson.objects.get(slug=slug)
        cache.set(lesson_cache_key, lesson, 60 * 60)
        cache.set('lesson_detail_slug_cache', slug, 60 * 60)

    user_lesson_completed_cache_key = f'user_lesson_completed_cache_{slug}'
    user_lessons_completed = cache.get(user_lesson_completed_cache_key)
    if not user_lessons_completed:
        user_lessons_completed = {ul.lesson.id: ul.completed for ul in UserLessonRelation.objects.filter(  # (левый bar в lesson-detail)
            user=request.user, lesson__course=lesson.course).select_related('lesson')}
        cache.set(user_lesson_completed_cache_key, user_lessons_completed, 60 * 60)

    comments = LessonComment.objects.filter(lesson=lesson).select_related('lesson', 'user')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = form.cleaned_data['comment']
            new_comment = LessonComment.objects.create(comment=comment, lesson=lesson, user=user)
            new_comment.save()
            lesson_detail_cache_delete()
            return redirect('courses:lesson_detail', slug)
    else:
        form = CommentForm()

    context = {'lesson': lesson, 'user_lessons_completed': user_lessons_completed,
               'comments': comments, 'form': form}

    return render(request, 'lessons/detail.html', context=context)


def courses_list_view(request: HttpRequest):
    search_query = request.GET.get('search', '').strip()  # по дефолту ''

    cache_key = f'course_cache_{search_query}' if search_query else settings.COURSE_CACHE

    courses = cache.get(cache_key)
    if not courses:
        if search_query:
            courses = Course.objects.filter(title__icontains=search_query,
                                            owner__username__icontains=search_query
                                            ).prefetch_related(Prefetch('owner', queryset=User.objects.all().only('username')))
            cache.set('course_cache_query', search_query, 60 * 60)
        else:
            courses = Course.objects.all().prefetch_related(Prefetch('owner', queryset=User.objects.all().only('username')))
        cache.set(cache_key, courses, 60 * 60)

    paginator = Paginator(courses, 60 * 60)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'courses/list.html',
                  {'courses': page_obj})


def course_detail_view(request: HttpRequest, slug):
    cache_key = f'course_detail_{slug}'
    course = cache.get(cache_key)
    if not course:
        course = Course.objects.get(slug=slug)
        cache.set('course_detail_slug_cache', slug, 60 * 60)
        cache.set(cache_key, course, 60 * 60)
    return render(request,
                  'courses/detail.html',
                  {'course': course})


@login_required
def user_enroll_to_course_view(request: HttpRequest, slug):
    user = request.user
    course = Course.objects.get(slug=slug)
    if user not in course.students.all():
        UserCourseRelation.objects.create(user=user,
                                          course=course,
                                          enrolled=True)
    return redirect('courses:course_detail', slug)
