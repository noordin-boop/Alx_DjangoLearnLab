from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for managing the CustomUser model.
    """
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional Info",
            {"fields": ("date_of_birth", "profile_photo")},
        ),
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            "Additional Info",
            {"fields": ("date_of_birth", "profile_photo")},
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
