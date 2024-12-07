from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.(request handler)
def say_hello(request):
    return HttpResponse('Hello Django')

def say_hi(request):
    return render(request, 'hi.html', {'name': 'LJ Ventanilla'})

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_list.html', {'blog_list': posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog_detail.html', {'post': post})
