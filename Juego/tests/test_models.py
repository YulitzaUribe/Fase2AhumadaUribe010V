from django.test import TestCase
from Juego.models import Post
import os

class PostModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Post.objects.create(id='44fc2b9d-2b04-45cb-af8a-c4601527b156', title='test',content='testing123')

	def test_title_label(self):
		post=Post.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
		field_label = post.meta.get_field('title').verbose_name
		self.assertEquals(field_label,'title')

	def test_content_label(self):
		post=Post.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
		field_label = post.meta.get_field('content').verbose_name
		self.assertEquals(field_label,'title')

	def test_title_max_length(self):
		post=Post.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
		field_label = post.meta.get_field('title').max_lenght
		self.assertEquals(max_lenght,100)

	def test_content_max_length(self):
		post=Post.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
		field_label = post.meta.get_field('content').max_lenght
		self.assertEquals(max_lenght,1000)

	def test_get_absolute_url(self):
        post=Post.objects.get(id='44fc2b9d-2b04-45cb-af8a-c4601527b156')
        self.assertEquals(post.get_absolute_url(), '/Juego/posts/44fc2b9d-2b04-45cb-af8a-c4601527b156')