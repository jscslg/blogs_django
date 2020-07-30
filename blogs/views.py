from django.shortcuts import render
from .models import Post

def home_view(request):
    context= {
        'posts':Post.objects.all()
    }
    return render(request,'blogs/home.html',context)

def about_view(request):
    return render(request,'blogs/about.html',{})