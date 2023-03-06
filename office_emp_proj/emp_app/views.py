from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from .models import Post
from django.views.generic.base import (
    TemplateView,
    RedirectView,
)
from django.db.models import F


class Ex2View(TemplateView):
    template_name = "index.html"
    # template_engine=""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class SinglePostView(TemplateView):
    template_name = "single_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        return context
