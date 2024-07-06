from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator


def my_courses_view(request):
    courses = request.user.courses.filter(active=True)
    paginator = Paginator(courses, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_courses.html', {'courses': page_obj})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('courses:course_list')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
