from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def path_to_profile_avatar(instance: "Profile", filename: str) -> str:
    return f'avatars/{instance.user.pk}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile",
                                on_delete=models.CASCADE)
    avatar = ProcessedImageField(upload_to=path_to_profile_avatar,
                            processors=[ResizeToFill(150, 150)],
                            options={'quality': 60}, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, default='')
    registered = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('img/no_image_profile.jpg')
