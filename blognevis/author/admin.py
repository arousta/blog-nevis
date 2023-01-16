from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from blognevis.core.admin import BlogNevisAdmin
from blognevis.core.constants import BLOGGERS_ADMINSITE_GROUP
from .models import Author


@admin.register(Author)
class BlogNevisUserAdmin(BlogNevisAdmin, UserAdmin):
    readonly_fields = ["date_joined", *BlogNevisAdmin.readonly_fields]

    def save_model(self, request, obj, form, change):
        """Automatically add user to the Bloggers group and give staff status when it's created via the admin site"""
        obj.is_staff = True
        super().save_model(request, obj, form, change)
        obj.groups.add(Group.objects.get(name=BLOGGERS_ADMINSITE_GROUP))
