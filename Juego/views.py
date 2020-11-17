from django.shortcuts import render
from django.views import generic
# Create your views here.
def index(request):


	return render(
		request,
		'index.html',
		)

def Login(request):

	return render(
		request,
		'Login.html',
		)

def Registrar(request):

	return render(
		request,
		'Registrar.html',
		)

from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class PostListView(generic.ListView):
	model = Post

class PostDetailView(generic.DetailView):
	model = Post

class PostCreate(CreateView):
	model = Post
	fields= ['title','content','image']

class PostUpdate(UpdateView):
	model = Post
	fields= ['title','content','image']

class PostDelete(DeleteView):
	model = Post
	