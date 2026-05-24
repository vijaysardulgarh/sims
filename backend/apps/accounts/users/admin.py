from django.contrib import admin

from django.contrib.auth.admin import (
    UserAdmin
)

from apps.accounts.users.models import (
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

        "school",

        "is_staff",

        "is_superuser",

        "is_active",

        "created_at",
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

        "school__name",
    )

    # =====================================
    # FILTERS
    # =====================================

    list_filter = (

        "school",

        "is_staff",

        "is_superuser",

        "is_active",

        "is_deleted",
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

        "created_at",

        "updated_at",

        "created_by",

        "updated_by",
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
            "School Information",

            {
                "fields": (
                    "school",
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

        (
            "Audit Information",

            {
                "fields": (

                    "created_at",

                    "updated_at",

                    "created_by",

                    "updated_by",
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

                    "school",

                    "password1",

                    "password2",

                    "is_active",

                    "is_staff",

                    "is_superuser",
                ),
            }
        ),
    )

    # =====================================
    # SAVE MODEL
    # =====================================

    def save_model(
        self,
        request,
        obj,
        form,
        change
    ):

        if not change:

            obj.created_by = (
                request.user
            )

        obj.updated_by = (
            request.user
        )

        super().save_model(

            request,

            obj,

            form,

            change
        )