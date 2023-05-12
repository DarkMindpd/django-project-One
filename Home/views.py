from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required

def Home(request):
     p = Post.objects.all()
     post = {}
     for i in p:
          a = i.like.filter().order_by('-id')[:2][::-1]
          post[i] = a
     print([(post.items)])
     return render(request, 'Home\home.html', {"post" : post})



