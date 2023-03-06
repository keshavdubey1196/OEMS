from django.urls import path

# from . import views
from django.views.generic import TemplateView
from .views import (
    Ex2View,
    SinglePostView,
)


app_name = "emp_app"

urlpatterns = [
    path("", Ex2View.as_view(), name="posts"),
    path("single_post/<str:pk>/", SinglePostView.as_view(), name="single-post"),
]
