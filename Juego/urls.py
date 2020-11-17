from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('Login/',views.Login,name='Login'),
	path('Registrar/',views.Registrar,name='Registrar'),
	path('posts/',views.PostListView.as_view(),name='posts'),
	path('posts/<str:pk>',views.PostDetailView.as_view(), name='post-detail'),

]

urlpatterns += [
	path('posts/create/', views.PostCreate.as_view(),name='post_create'),
	path('posts/<str:pk>/update/',views.PostUpdate.as_view(),name='post_update'),
	path('posts/<str:pk>/delete/',views.PostDelete.as_view(),name='post_delete'),
]