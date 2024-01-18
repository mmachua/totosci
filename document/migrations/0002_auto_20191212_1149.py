# Generated by Django 2.0.7 on 2019-12-12 08:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
