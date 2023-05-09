from django.shortcuts import render
from accounts.models import User
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required(login_url='enter_acc')
def add_post(request):
    if request.method == "GET":
        u = request.user
        print(u.username)
        return render(request, 'new_post\page_add.html', {"u" : u})
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            '''new_post_img = request.POST['post_img']
            new_post_title = request.POST['title']
            new_post_body = request.POST['body']
            new_post_tag = request.POST['tags']
            Post.objects.create(
                post_img = new_post_img,
                tag = new_post_tag,
                title = new_post_title,
                body = new_post_body,
                user = request.user
                )'''
        p = Post.objects.all()
        return render(request, 'Home\home.html', {"post" : p})
