from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import register


def Home(request):
     p = Post.objects.all()
     pl = {}
     for i in p:
          a = i.like.filter().order_by('-id')[:2][::-1]
          pl[i] = a
     print(pl.get)
     return render(request, 'Home\home.html', {"post" : pl})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


