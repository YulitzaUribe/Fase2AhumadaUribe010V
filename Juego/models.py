from django.db import models
from django.urls import reverse
import uuid



class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	date = models.DateField(auto_now=True)
	image = models.ImageField()
	

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.title 




class Commentary(models.Model):
	post_id = models.ForeignKey(Post,on_delete = models.CASCADE)
	user = models.IntegerField()
	content = models.CharField(max_length=200)
	date = models.DateField(auto_now=True)

	def __str__(self):
		return self.user


