# Generated by Django 4.1.13 on 2024-07-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_remove_lessoncomment_user_lesson_relation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessoncomment',
            options={'ordering': ['-created']},
        ),
    ]
