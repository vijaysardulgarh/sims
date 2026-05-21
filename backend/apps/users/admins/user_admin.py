from django.contrib import admin

from django.contrib.auth.admin import (
    UserAdmin
)

from apps.users.models.user_model import (
    User
)


# ==========================================
# USER ADMIN
# ==========================================

@admin.register(User)
class CustomUserAdmin(
    UserAdmin
):

    model = User


    # =====================================
    # TABLE DISPLAY
    # =====================================

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


    # =====================================
    # SEARCH
    # =====================================

    search_fields = (

        "email",

        "username",

        "first_name",

        "last_name",
    )


    # =====================================
    # FILTERS
    # =====================================

    list_filter = (

        "is_staff",

        "is_superuser",

        "is_active",
    )


    # =====================================
    # ORDERING
    # =====================================

    ordering = (
        "email",
    )


    # =====================================
    # PAGINATION
    # =====================================

    list_per_page = 25


    # =====================================
    # READONLY FIELDS
    # =====================================

    readonly_fields = (

        "last_login",

        "date_joined",
    )


    # =====================================
    # FIELDSETS
    # =====================================

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
            "Personal Information",
            {
                "fields": (

                    "first_name",

                    "last_name",

                    "phone",

                    "profile_photo",

                    "designation",
                )
            }
        ),

        (
            "Verification",
            {
                "fields": (

                    "is_email_verified",

                    "is_phone_verified",
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

                    "last_password_changed_at",
                )
            }
        ),
    )


    # =====================================
    # ADD USER FORM
    # =====================================

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

                    "is_active",

                    "is_staff",

                    "is_superuser",
                ),
            }
        ),
    )