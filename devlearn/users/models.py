from django.db import models
from django.contrib.auth.models import User


def path_to_profile_avatar(instance, filename):
    return f'avatars/{instance.pk}/{filename}'



class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile",
                                on_delete=models.CASCADE)
    avatar = models.FileField(upload_to=path_to_profile_avatar, null=True)
    bio = models.TextField(max_length=500, blank=True, default='')
    email = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
    
