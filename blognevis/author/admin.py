from .models import Author

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


admin.register(Author, UserAdmin)
