from django.shortcuts import render
from .models import blog_post

# Create your views here.
def home(request):
	all = blog_post.objects.all().order_by('-date')[0:1]
	two = blog_post.objects.all().order_by('-date')[0:4]
	thr = blog_post.objects.filter(pick=2).order_by('-date')[0:1]
	four = blog_post.objects.filter(pick=2).order_by('-date')[0:4]
	return render(request, ("base/home.html"), {
			'all': all,
			'two': two,
			'thr': thr,
			'four': four
		})

def about(request, number, topic):
	alle = blog_post.objects.all()
	appl = blog_post.objects.get(topic=topic)
	return render(request, ("base/about.html"), {
		'alle': alle,
		'appl': appl
	})


def every(request):
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/every.html"), {
		'all':  all
	})

