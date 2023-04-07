from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

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
                u = User.objects.create(username=user_name, email=mail)
                u.set_password(password1)
                u.first_name = first_name
                u.last_name = last_name
                u.save()
                return redirect('successful_singup')
            else:
                print('wrong pass')
        else:
            pass_word = request.POST.get('login_pass')
            user_name = request.POST.get('login_username')
            
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request,user=user)
                return redirect('Home')
            else:
                return render(request, 'accounts/index.html', {})
    else:
        return render(request, 'accounts/index.html', {})
