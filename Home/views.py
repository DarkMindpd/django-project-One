from django.shortcuts import render
from .models import Post

def Home(request):
     p = Post.objects.all()
     return render(request, 'Home\home.html', {"post" : p})

def post_details(request,pk):
    p = Post.objects.get(id=pk)
    return render(request,'Home\post_details.html',{'p':p})
