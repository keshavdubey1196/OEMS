from django.urls import path
from . import views

app_name = "emp_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("<slug:post>/", views.single_post, name="single_post"),
]
