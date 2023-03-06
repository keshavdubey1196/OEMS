from django.test import TestCase
from emp_app.models import Post
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint


class TestAllModels(TestCase):
    # Test all the models

    def setUp(self):
        test_owner = User.objects.create(
            username="test_owner",
            password="test_password",
        )
        self.post_obj = Post.objects.create(
            owner=test_owner,
            title="test title",
            content="test content",
        )

    def test_title_of_post(self):
        self.assertEqual(str(self.post_obj), "test title")

    def test_likes_on_post(self):
        testUser1 = User.objects.create(
            username="testUser1",
            password="testPassword",
        )
        self.post_obj.likes.set([testUser1.pk])

        self.assertEqual(self.post_obj.likes.count(), 1)
