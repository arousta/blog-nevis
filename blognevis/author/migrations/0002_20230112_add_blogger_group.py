# Generated by Django 4.1.4 on 2023-01-12 06:32

from django.db import migrations
from blognevis.core.constants import BLOGGERS_ADMINSITE_GROUP

BLOGGERS = BLOGGERS_ADMINSITE_GROUP


def create_blogger_group_and_give_permissions(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    permissions = Permission.objects.filter(
        content_type__app_label="post",
        content_type__model="post",
        codename__regex="^(add|change|delete|view)_",
    )
    blog_writers = Group.objects.create(name=BLOGGERS)
    blog_writers.permissions.set(permissions)


def remove_blogger_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name=BLOGGERS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_blogger_group_and_give_permissions, remove_blogger_group
        ),
    ]
