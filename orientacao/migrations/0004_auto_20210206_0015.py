# Generated by Django 3.0.2 on 2021-02-06 03:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orientacao', '0003_auto_20210131_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orientacao',
            name='orientandos',
        ),
        migrations.RemoveField(
            model_name='orientacao',
            name='user',
        ),
        migrations.AddField(
            model_name='orientacao',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='usuarios', to=settings.AUTH_USER_MODEL),
        ),
    ]
