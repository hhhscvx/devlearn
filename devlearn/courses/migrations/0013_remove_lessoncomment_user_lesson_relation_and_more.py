# Generated by Django 4.1.13 on 2024-07-03 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0012_remove_usercourserelation_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessoncomment',
            name='user_lesson_relation',
        ),
        migrations.AddField(
            model_name='lessoncomment',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.lesson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessoncomment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
