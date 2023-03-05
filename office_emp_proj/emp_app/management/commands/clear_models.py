from django.core.management.base import BaseCommand
from emp_app import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Post.objects.all().delete()
