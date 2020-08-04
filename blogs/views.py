from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

def home_view(request):
    context= {
        'posts' : Post.objects.all()
    }
    return render(request,'blogs/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='blogs/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post
    template_name='blogs/home.html'
    context_object_name='posts'
    ordering=['-date_posted']

def about_view(request):
    return render(request,'blogs/about.html',{})