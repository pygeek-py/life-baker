from django.db import models

# Create your models here.
class category(models.Model):
	cate = models.CharField(max_length=1000)

	def __str__(self):
		return self.cate

class blog_post(models.Model):
	pick = models.ManyToManyField(category, related_name="pick")
	img = models.ImageField(upload_to='images/')
	topic = models.CharField(max_length=10000)
	header = models.CharField(max_length=10000, null=True)
	subtopic = models.CharField(max_length=1000)
	description = models.TextField(max_length=1000000000)
	date = models.DateTimeField(auto_now_add=True)
	number = models.IntegerField()