from django.test import TestCase
from django.urls import reverse

from blognevis.core.constants import BLOGGERS_ADMINSITE_GROUP
from .models import Author


class AuthorTests(TestCase):
    def test_authors_get_proper_permissions_when_added_via_adminsite(self):
        admin = Author.objects.create_superuser("admin", "admin@blognevis.ca", "123")
        self.client.force_login(admin)
        self.client.post(
            reverse("admin:author_author_add"),
            data={
                "username": "writer1",
                "password1": "A2Z-auto",
                "password2": "A2Z-auto",
            },
        )

        # make sure created blogger can login and is added to the bloggers group
        user = Author.objects.get(username="writer1")
        self.assertTrue(user.is_staff)
        user.groups.get(name=BLOGGERS_ADMINSITE_GROUP)

    def test_author_instance_soft_delete(self):
        user = Author.objects.create_user("ali")
        user.delete()
        user.refresh_from_db()
        self.assertFalse(user.is_active)

    def test_author_queryset_soft_delete(self):
        user = Author.objects.create_user("ali")
        Author.objects.filter(username="ali").delete()
        user.refresh_from_db()
        self.assertFalse(user.is_active)
