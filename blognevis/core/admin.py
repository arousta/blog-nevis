from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django import forms


class BlogNevisAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "deleted_at", "created", "modified"]
    formfield_overrides = {ArrayField: {"widget": forms.Textarea}}
