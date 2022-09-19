from django.shortcuts import render
from .models import blog_post, review
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

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
	adds = appl.review_set.all()
	if request.method == "POST":
		name = request.POST['person']
		email = request.POST['email']
		body = request.POST['body']
		c = review(join=appl, name=name, email=email, comment=body)
		c.save()
		return HttpResponseRedirect(reverse("home"))
	return render(request, ("base/about.html"), {
		'alle': alle,
		'appl': appl,
		'adds': adds
	})


def every(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/every.html"), {
		'all':  all,
		'adr': adr
	})

def latest(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/latest.html"), {
		'all':  all,
		'adr': adr
	})

def sport(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/sport.html"), {
		'all':  all,
		'adr': adr
	})

def computer(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/computer.html"), {
		'all':  all,
		'adr': adr
	})

def examination(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/examination.html"), {
		'all':  all,
		'adr': adr
	})

def hall(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/hall.html"), {
		'all':  all,
		'adr': adr
	})

def enter(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/enter.html"), {
		'all':  all,
		'adr': adr
	})

def academic(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/academic.html"), {
		'all':  all,
		'adr': adr
	})

def megaphone(request):
	adr = blog_post.objects.all().order_by('-date')[0:1]
	all = blog_post.objects.all().order_by('-date')
	return render(request, ("base/megaphone.html"), {
		'all':  all,
		'adr': adr
	})
