from django.shortcuts import render
from .models import Post

# Create your views here.

def Home(request):
    p = Post.objects.all()
    return render(request, 'Home\home.html', {"post" : p})

def post_details(request,id):
    p = Post.objects.get(id=id)
    return render(request,'Home\post_details.html',{'p':p})
