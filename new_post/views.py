from django.shortcuts import render
from Home.models import User
from Home.models import Post

def add_post(request):
    if request.method == "GET":
        u = User.objects.get(id=1)
        return render(request, 'new_post\page_add.html', {"user" : u})
    elif request.method == "POST":
        new_post_img = request.POST['new_post_img']
        new_post_title = request.POST['new_post_title']
        new_post_body = request.POST['new_post_body']
        new_post_tag = request.POST['new_post_tag']
        Post.objects.create(
            tag = new_post_tag,
            title = new_post_title,
            body = new_post_body,
            user_name = User.objects.get(id=1)
            )
        p = Post.objects.all()
        return render(request, 'Home\home.html', {"post" : p})

