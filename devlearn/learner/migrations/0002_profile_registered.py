# Generated by Django 4.1.13 on 2024-07-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='registered',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
