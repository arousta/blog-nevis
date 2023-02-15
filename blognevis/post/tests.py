from django.test import TestCase
from django.urls import reverse

from blognevis.author.factories import BloggerFactory
from .models import Post


class PostAdminViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.blogger = BloggerFactory()

    def test_author_set_automatically_when_creating_post_via_adminsite(self):
        self.client.force_login(self.blogger)
        self.client.post(
            reverse("admin:post_post_add"),
            data={
                "title": "django",
                "text": "blah",
            },
        )

        # only sent title/text through form data, but the author should automatically be set
        Post.objects.get(title="django", text="blah", author=self.blogger)
