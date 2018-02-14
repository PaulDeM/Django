from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_detail(request, slug):
    #return HttpResponse(request, slug)
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/posts_detail.html', {'post': post})

