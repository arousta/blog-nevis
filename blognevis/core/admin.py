from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django import forms


class BlogNevisAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "deleted_at", "created", "modified"]
    formfield_overrides = {ArrayField: {"widget": forms.Textarea}}

    # def has_module_permission(self, request):
    #     # Authors only need (should) access to Post admin. Other apps only accessible by suepruser
    #     return ( request.user.is_superuser or self.opts.app_label=="post" )
