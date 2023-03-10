from django.urls import path
from Home import views
from .models import Post

urlpatterns = [
    path('', views.Home, name='Home'),
    path('posts/<int:id>', views.post_details, name='post')
]

