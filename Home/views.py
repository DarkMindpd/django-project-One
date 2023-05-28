from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required  


def Home(request):
     p = Post.objects.all().order_by('-id')
     pl = {}
     for i in p:
          a = i.like.filter().order_by('-id')[:4]
          pl[i] = a
     return render(request, 'Home\home.html', {"post" : pl})

