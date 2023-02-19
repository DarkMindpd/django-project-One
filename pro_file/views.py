from django.shortcuts import render

# Create your views here.

def pro_file(request):
    return render(request,'profile\profile.html',{})