# Generated by Django 4.1.13 on 2024-07-03 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlessonrelation',
            name='comment',
        ),
        migrations.CreateModel(
            name='LessonComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_lesson_relation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.userlessonrelation')),
            ],
        ),
    ]
