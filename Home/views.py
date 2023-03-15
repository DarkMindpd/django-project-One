from django.shortcuts import render
from .models import Post
from .models import User

# Create your views here.

def Home(request):
        p = Post.objects.all()
        return render(request, 'Home\home.html', {"post" : p})

def add_post(request):
    if request.method == "GET":
        u = User.objects.all()
        return render(request, 'Home\add_post.html', {"user" : u})
    elif request.method == "POST":

        return


def post_details(request,pk):
    p = Post.objects.get(id=pk)
    return render(request,'Home\post_details.html',{'p':p})
