from django.urls import path
from new_post import views

urlpatterns = [
    path('new_post', views.add_post, name='add_post')
]