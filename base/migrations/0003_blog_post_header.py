# Generated by Django 3.2.13 on 2022-09-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220916_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='header',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
