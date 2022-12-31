from .models import Post

from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["author"]
