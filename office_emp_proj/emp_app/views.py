from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from .models import Post

# Create your views here.


def home(request):
    all_posts = Post.objects.all()
    return render(request, "index.html", {"posts": all_posts})


def single_post(request, post):
    post = get_object_or_404(Post, slug=post)

    return render(request, "single_post.html", {"post": post})
