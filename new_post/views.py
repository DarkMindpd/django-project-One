from django.shortcuts import render
from Home.models import User
from Home.models import Post

def add_post(request):
    if request.method == "GET":
        u = User.objects.all()
        return render(request, 'new_post\page_add.html', {"user" : u})
    elif request.method == "POST":
        a = Post()
        a.body=request.POST["new_post"]
        a.user_name=1
        a.save()
        return
