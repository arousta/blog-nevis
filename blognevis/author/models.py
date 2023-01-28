from utility.models import TimeStampedUUIDMixin, UserSoftDeleteQuerySet
from django.contrib.auth.models import AbstractUser, UserManager


# Here we have custome manager of User class by django. But also want to have a custome queryset
# that does a soft delete by setting is_active=False. We use this technique:
# https://docs.djangoproject.com/en/4.1/topics/db/managers/#from-queryset
class AuthorManager(UserManager.from_queryset(UserSoftDeleteQuerySet)):
    pass


class Author(AbstractUser, TimeStampedUUIDMixin):
    objects = AuthorManager()

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save(update_fields=["is_active"])
