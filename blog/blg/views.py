from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blg/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug_iexact=slug) #получает из бд ссылку
    render(request, 'blog/post_detail.html', context={'post': post})