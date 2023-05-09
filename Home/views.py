from django.shortcuts import render
from post.models import Post
from django.contrib.auth.decorators import login_required

def Home(request):
     p = Post.objects.all()
     return render(request, 'Home\home.html', {"post" : p})


@login_required(login_url='enter_acc')
def post_details(request,pk):
    p = Post.objects.get(id=pk)
    return render(request,'Home\post&comment.html',{'p':p})
