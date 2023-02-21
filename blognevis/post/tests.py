from django.test import TestCase
from django.urls import reverse

from blognevis.author.factories import BloggerFactory
from .models import Post


class PostViewTests(TestCase):
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

        # we only provided title/text, but author should be set automatically
        Post.objects.get(title="django", text="blah", author=self.blogger)
