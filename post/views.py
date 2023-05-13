from django.shortcuts import render, get_object_or_404
from accounts.models import User
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from Home.views import Home

@login_required(login_url='enter_acc')
def add_post(request):
    if request.method == "GET":
        u = request.user
        print(u.username)
        return render(request, 'new_post\page_add.html', {"u" : u})
    elif request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            print(post.post_img)
            post.save()
        p = Post.objects.all()
        return HttpResponseRedirect(reverse(Home))
    



@login_required(login_url='enter_acc')
def post_details(request,pk):

    p = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = p
            comment.user = request.user
            comment.save()
    return render(request,'post\post&comment.html',{'p':p})




@login_required(login_url='enter_acc')
def PostLike(request, pk):
    post = Post.objects.get(id = pk)
    user = request.user
    if post.like.filter(id = user.id).exists():
        post.like.remove(user)
    else:
        post.like.add(user)
    return HttpResponseRedirect(reverse(post_details, args=[pk]))