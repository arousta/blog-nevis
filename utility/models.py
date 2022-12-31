from django.db import models
from django_softdelete.models import SoftDeleteModel
from django_softdelete.mangers import SoftDeleteManager  # noqa
import uuid


class UUIDPrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedSoftDeleteUUIDMixin(
    SoftDeleteModel, TimeStampedMixin, UUIDPrimaryKeyMixin
):
    _soft_delete_cascade = True
    _restore_soft_deleted_related_objects = True

    class Meta:
        abstract = True
