from django.urls import path
from Home import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('posts/<int:pk>', views.post_details, name='post')
]

