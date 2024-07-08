from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile


def profile_view(request, username):  # TODO отображать список пройденных курсов
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    return render(request,
                  'learner/profile.html',
                  {'profile': profile})
