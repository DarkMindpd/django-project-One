from django.urls import path
from pro_file import views

urlpatterns = [
    path('', views.pro_file),
]