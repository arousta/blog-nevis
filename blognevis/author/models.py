from utility.models import TimeStampedSoftDeleteUUIDMixin, SoftDeleteManager
from django.contrib.auth.models import AbstractUser, UserManager


class AuthorManager(UserManager, SoftDeleteManager):
    pass


class Author(AbstractUser, TimeStampedSoftDeleteUUIDMixin):
    objects = AuthorManager()
