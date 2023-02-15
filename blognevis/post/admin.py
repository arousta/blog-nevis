from django.contrib import admin

from blognevis.core.admin import BlogNevisAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(BlogNevisAdmin):

    fieldsets = [
        (None, {"fields": ("id",)}),
        ("Post content", {"fields": ("title", "text")}),
        ("Timestamps", {"fields": ("created", "modified")}),
        ("Soft delete status", {"fields": ("is_deleted", "deleted_at")}),
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Authors should only see/edit their own posts
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
