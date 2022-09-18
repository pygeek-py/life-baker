from django.contrib import admin
from .models import blog_post, category
# Register your models here.

admin.site.register(blog_post)
admin.site.register(category)