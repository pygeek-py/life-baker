# Generated by Django 3.2.13 on 2022-09-19 17:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_blog_post_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='like',
            field=models.ManyToManyField(null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
