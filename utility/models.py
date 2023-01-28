from django.db import models
from django_softdelete.models import SoftDeleteModel
from django_softdelete.mangers import SoftDeleteManager  # noqa
import uuid


# ------------------- QuerySets
class UserSoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        # We don't delete users, just set is_active=False, as suggested in:
        # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.is_active
        return self.update(is_active=False)


# ------------------- Models
class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedSoftDeleteUUIDMixin(SoftDeleteModel, TimeStampedMixin, UUIDPrimaryKeyMixin):
    _soft_delete_cascade = True
    _restore_soft_deleted_related_objects = True

    class Meta:
        abstract = True
