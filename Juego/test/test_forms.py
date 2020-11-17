from django.test import TestCase
from Juego.forms import PostForm
from Juego.models import Post
from django.core.files.uploadedfile import SimpleUploadedFile

class PostFormsTest(TestCase):
    def test_valid_form(self):
        post = Post.objects.create(title='test1', content='testing')
        data = {'title': post.title, 'content': post.content,}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        post = Post.objects.create(title='', content='')
        data = {'title': post.title, 'content': post.content,}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())