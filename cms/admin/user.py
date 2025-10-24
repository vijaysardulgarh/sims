from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ..models.user import User
from ..resources.user import UserResource

@admin.register(User)
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    resource_class = UserResource

    fieldsets = BaseUserAdmin.fieldsets + (
        ("School Info", {"fields": ("school", "role")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("School Info", {"fields": ("school", "role")}),
    )

    list_display = ("username", "email", "school", "role", "is_staff", "is_active")
    list_filter = ("school", "role", "is_staff", "is_active")
    search_fields = ("username", "email")