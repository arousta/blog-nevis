from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from blognevis.core.admin import BlogNevisAdmin
from .models import Author


@admin.register(Author)
class BlogNevisUserAdmin(BlogNevisAdmin, UserAdmin):
    readonly_fields = ["date_joined"]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # add premissions


# admin.site.register(Author, BlogNevisUserAdmin)
