from django.contrib import admin

from django.contrib.auth.admin import (
    UserAdmin
)

from .models import (
    User,
    Role,
    Permission,
    UserRole,
    RolePermission
)


# ==========================================
# USER ADMIN
# ==========================================

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # ==========================================
    # TABLE DISPLAY
    # ==========================================

    list_display = (
        "id",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    list_display_links = (
        "id",
        "email",
    )

    # ==========================================
    # SEARCH
    # ==========================================

    search_fields = (
        "email",
        "username",
    )

    # ==========================================
    # FILTERS
    # ==========================================

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )

    # ==========================================
    # ORDERING
    # ==========================================

    ordering = (
        "email",
    )

    # ==========================================
    # PAGINATION
    # ==========================================

    list_per_page = 25

    # ==========================================
    # READONLY FIELDS
    # ==========================================

    readonly_fields = (
        "last_login",
        "date_joined",
    )

    # ==========================================
    # FIELDSETS
    # ==========================================

    fieldsets = (

        (
            "Login Credentials",
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                )
            }
        ),

        (
            "Profile Links",
            {
                "fields": (
                    "staff",
                    "student",
                )
            }
        ),

        (
            "Extra Info",
            {
                "fields": (
                    "phone",
                    "profile_photo",
                    "designation",
                    "is_email_verified",
                    "is_phone_verified",
                    "last_password_changed_at",
                )
            }
        ),

        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            }
        ),

        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            }
        ),
    )

    # ==========================================
    # ADD USER FORM
    # ==========================================

    add_fieldsets = (

        (
            "Create User",
            {
                "classes": (
                    "wide",
                ),

                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "staff",
                    "student",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            }
        ),
    )


# ==========================================
# ROLE ADMIN
# ==========================================

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "is_active",
    )


# ==========================================
# PERMISSION ADMIN
# ==========================================

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "module",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "module",
        "is_active",
    )


# ==========================================
# USER ROLE ADMIN
# ==========================================

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "role",
        "is_active",
    )

    list_filter = (
        "role",
        "is_active",
    )

    search_fields = (
        "user__email",
        "role__name",
    )


# ==========================================
# ROLE PERMISSION ADMIN
# ==========================================

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):

    list_display = (
        "role",
        "permission",
        "is_active",
    )

    list_filter = (
        "role",
        "permission",
    )

    search_fields = (
        "role__name",
        "permission__name",
    )