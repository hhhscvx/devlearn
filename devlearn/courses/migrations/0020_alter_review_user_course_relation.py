# Generated by Django 4.1.13 on 2024-07-08 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_remove_usercourserelation_rate_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_course_relation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='review', to='courses.usercourserelation'),
        ),
    ]
