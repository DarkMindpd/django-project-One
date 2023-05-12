from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import get_object_or_404 
from .models import User_profile
from django.urls import reverse
from post.models import Post

def enter_acc(request):
    if request.method == 'POST':
        if 'user_first_name' in request.POST:
            user_name = request.POST.get('username')
            mail = request.POST.get('user_mail')
            first_name = request.POST.get('user_first_name')
            last_name = request.POST.get('user_last_name')
            password1= request.POST.get('user_pass1')
            password2= request.POST.get('user_pass2')
            if password1 == password2 :
                if len(User.objects.filter(username=user_name)) == 0 and len(User.objects.filter(email=mail)) == 0:
                    u = User.objects.create(username=user_name, email=mail)
                    u.set_password(password1)
                    u.first_name = first_name
                    u.last_name = last_name
                    u.save()
                    return redirect('successful_singup')
                else:
                    messages.add_message(request, messages.ERROR, "Your account is already exists.")
                    return render(request, 'accounts/index.html', {})
            else:
                messages.add_message(request, messages.ERROR, "Passwords don't match.")
                return render(request, 'accounts/index.html', {})
        else:
            pass_word = request.POST.get('login_pass')
            user_name = request.POST.get('login_username')
            
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request,user=user)
                return redirect('Home')
            else:
                messages.add_message(request, messages.ERROR, "Somthing went wrong with your Inputs.")
                return render(request, 'accounts/index.html', {})
    else:
        return render(request, 'accounts/index.html', {})


def log_out(request):
    logout(request)
    return render(request, 'accounts\index_success_logout.html', {})



def profile_detail(request, username):
    user = get_object_or_404(User_profile, user__username = username)
    post = User.objects.get(username = username).post_set.filter().order_by('-id')[:4][::-1]
    return render(request, 'accounts/profile_far_view.html', {'profile' : user , 'post' : post})

def profile_posts(request, username):
    post = User.objects.get(username = username).post_set.all()
    return render(request, 'accounts/profile_posts.html', {'post' : post})


def followToggle(request, author):
    author_user = User.objects.get(username = author)
    author_obj = User_profile.objects.get(user_id = (author_user.id))
    viewer_user = User.objects.get(username = request.user.username)
    viewer_obj = User_profile.objects.get(user_id = (viewer_user.id))
    following = author_obj.following.all()

    if not author == viewer_obj.user.username:
        if viewer_obj in following:
            author_obj.following.remove(viewer_obj.id)
        else:
            author_obj.following.add(viewer_obj.id)
    return HttpResponseRedirect(reverse(profile_detail, args=[author_obj.user.username]))

