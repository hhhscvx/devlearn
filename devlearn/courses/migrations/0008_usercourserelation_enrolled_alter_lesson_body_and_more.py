# Generated by Django 4.1.13 on 2024-06-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourserelation',
            name='enrolled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usercourserelation',
            name='comment',
            field=models.TextField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='usercourserelation',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None, null=True),
        ),
    ]
