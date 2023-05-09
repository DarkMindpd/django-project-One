from django.urls import path
from . import views

urlpatterns = [
    path('new_post', views.add_post, name='add_post'),
    path('post-like/<int:pk>', views.PostLike, name='postlike'),
]