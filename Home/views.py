from django.shortcuts import render
from .models import Post

# Create your views here.

def Home(request):
    p = Post.objects.all()
    return render(request, 'Home\home.html', {"post" : p})