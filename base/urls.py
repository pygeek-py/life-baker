from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('article/<str:number>/<str:topic>', views.about, name="article"),
    path('all/blogs/', views.every, name="every"),
    path('latest/blogs/', views.latest, name="latest"),
    path('sport/blogs/', views.sport, name="sport"),
    path('computer/blogs/', views.computer, name="computer"),
    path('examination/blogs/', views.examination, name="examination"),
    path('hall/blogs/', views.hall, name="hall"),
    path('enter/blogs/', views.enter, name="enter"),
    path('academic/blogs/', views.academic, name="academic"),
    path('megaphone/blogs/', views.megaphone, name="megaphone"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)