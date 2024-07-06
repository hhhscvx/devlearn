from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, UserCourseRelation, Lesson, UserLessonRelation, LessonComment
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.contrib.auth.models import User
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.http import HttpRequest, JsonResponse


def course_review_list(request: HttpRequest, course_id):
    user_course_list = UserCourseRelation.objects.filter(course_id=course_id, rate__isnull=False)
    return render(request, 'courses/course_review_list.html', {'user_courses': user_course_list})


def set_course_review(request: HttpRequest, course_id):
    user_id = request.user.id
    user_course = get_object_or_404(UserCourseRelation, user_id=user_id, course_id=course_id)
    if request.method == "POST":
        data = request.POST
        print(f'Request data: {data}')
        rate = data.get('rate')
        review = data.get('review')
        user_course.rate = rate
        user_course.review = review
        user_course.save()
        return redirect('courses:course_detail', user_course.course.slug)
    return JsonResponse({'success': True})


def lesson_comment_delete_view(request: HttpRequest, slug, pk):
    comment = LessonComment.objects.get(pk=pk)
    comment.delete()
    return redirect('courses:lesson_detail', slug)


def lesson_completed_view(request: HttpRequest, slug):
    lesson = Lesson.objects.get(slug=slug)
    user_lesson, _ = UserLessonRelation.objects.get_or_create(user=request.user, lesson=lesson)
    user_lesson.completed = True
    user_lesson.save(updated_by=request.user.id)
    return redirect('courses:lesson_detail', slug)


@login_required
def lesson_detail_view(request: HttpRequest, slug):
    lesson = Lesson.objects.select_related('course').get(slug=slug)

    user_lessons_completed = {ul.lesson.id: ul.completed for ul in UserLessonRelation.objects.filter(
        user=request.user, lesson__course=lesson.course).select_related('lesson')}

    comments = LessonComment.objects.filter(lesson=lesson).select_related('user')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = form.cleaned_data['comment']
            new_comment = LessonComment.objects.create(comment=comment, lesson=lesson, user=user)
            new_comment.save()
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
            courses = Course.objects.filter(active=True).prefetch_related(Prefetch('owner', queryset=User.objects.all().only('username')))
        cache.set(cache_key, courses, 60 * 60)

    paginator = Paginator(courses, 60 * 60)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,
                  'courses/list.html',
                  {'courses': page_obj})


def course_detail_view(request: HttpRequest, slug):
    course = Course.objects.get(slug=slug)
    request_user_id = request.user.id
    user_course, _ = UserCourseRelation.objects.get_or_create(user_id=request_user_id, course_id=course.id)
    return render(request,
                  'courses/detail.html',
                  {'course': course, 'user_course': user_course})


@login_required
def user_enroll_to_course_view(request: HttpRequest, slug):
    user = request.user
    course = Course.objects.get(slug=slug)
    if user not in course.students.all():
        UserCourseRelation.objects.create(user=user,
                                          course=course,
                                          enrolled=True)
    return redirect('courses:course_detail', slug)
