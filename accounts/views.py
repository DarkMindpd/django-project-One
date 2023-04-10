from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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
                if User.objects.get(username=user_name) is None and User.objects.get(email=mail)is None:
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
