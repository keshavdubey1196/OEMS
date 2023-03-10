from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=250)
    content = models.TextField()
    likes = models.ManyToManyField(
        User,
        related_name="like",
        default=None,
        blank=True,
    )

    def __str__(self):
        return self.title
