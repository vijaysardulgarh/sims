from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # ==========================================
    # TABLE DISPLAY
    # ==========================================

    list_display = (
        'id',
        'email',
        'role',
        'school',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    list_display_links = (
        'id',
        'email',
    )

    # ==========================================
    # SEARCH
    # ==========================================

    search_fields = (
        'email',
        'username',
        'school__name',
    )

    # ==========================================
    # FILTERS
    # ==========================================

    list_filter = (
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
        'school',
    )

    # ==========================================
    # ORDERING
    # ==========================================

    ordering = (
        'school',
        'role',
        'email',
    )

    # ==========================================
    # PAGINATION
    # ==========================================

    list_per_page = 25

    # ==========================================
    # READONLY FIELDS
    # ==========================================

    readonly_fields = (
        'last_login',
        'date_joined',
    )

    # ==========================================
    # FIELDSETS
    # ==========================================

    fieldsets = (

        ('Login Credentials', {
            'fields': (
                'email',
                'username',
                'password',
            )
        }),

        ('Role & School', {
            'fields': (
                'role',
                'school',
            )
        }),

        ('Profile Links', {
            'fields': (
                'staff',
                'student',
            )
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        ('Important Dates', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )

    # ==========================================
    # ADD USER FORM
    # ==========================================

    add_fieldsets = (

        ('Create User', {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'role',
                'school',
                'staff',
                'student',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )