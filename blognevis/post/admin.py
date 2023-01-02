from .models import Post

from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django import forms


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "deleted_at", "created", "modified"]
    raw_id_fields = ["author"]
    formfield_overrides = {ArrayField: {"widget": forms.Textarea}}
    fieldsets = [
        (None, {"fields": ("id",)}),
        ("Post content", {"fields": ("author", "title", "text", "comments")}),
        ("Timestamps", {"fields": ("created", "modified")}),
        ("Soft delete status", {"fields": ("is_deleted", "deleted_at")}),
    ]
