from blognevis.author.models import Author
from utility.models import TimeStampedSoftDeleteUUIDMixin
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Post(TimeStampedSoftDeleteUUIDMixin):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    # For a light weight design, we assume the firs word in each comment represents the name of it's author
    comments = ArrayField(models.CharField(max_length=256), null=True)
    text = models.TextField()
    title = models.CharField(max_length=255)
