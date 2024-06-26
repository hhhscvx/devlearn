# Generated by Django 4.1.13 on 2024-06-20 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_usercourserelation_enrolled_alter_lesson_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourserelation',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserLessonRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, default=None, max_length=250, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
