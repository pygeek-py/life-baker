# Generated by Django 3.2.13 on 2022-09-19 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_blog_post_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('comment', models.CharField(max_length=1000)),
                ('join', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.blog_post')),
            ],
        ),
    ]