from django.contrib.auth.models import Group
from factory.django import DjangoModelFactory

from blognevis.core.constants import BLOGGERS_ADMINSITE_GROUP


class BloggerFactory(DjangoModelFactory):
    class Meta:
        model = "author.Author"

    is_staff = True
    first_name = "ali"
    last_name = "rosta"
    email = "ali@email.com"

    @classmethod
    def create(cls, **kwargs):
        # override this method to set the many to many relation (groups) after instance is created
        groups = kwargs.pop("groups", {})
        user = super().create(**kwargs)
        group_queryset = Group.objects.filter(name__in={*groups, BLOGGERS_ADMINSITE_GROUP})
        user.groups.set(group_queryset)

        return user
