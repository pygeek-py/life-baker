# Generated by Django 3.2.13 on 2022-09-19 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_blog_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='like',
        ),
    ]