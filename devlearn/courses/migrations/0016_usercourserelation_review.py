# Generated by Django 4.1.13 on 2024-07-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_course_discount_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourserelation',
            name='review',
            field=models.TextField(blank=True, default='', max_length=500, null=True),
        ),
    ]
