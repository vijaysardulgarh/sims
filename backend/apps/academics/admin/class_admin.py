from django.contrib import admin

from apps.academics.models import (
    Class,
    Stream,
    Medium,
    Classroom,
    Section,
)


# ==========================================
# CLASS
# ==========================================

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "school",
        "class_order",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "class_order",
        "name",
    )

    list_per_page = 25


# ==========================================
# STREAM
# ==========================================

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "school",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "name",
    )

    list_per_page = 25


# ==========================================
# MEDIUM
# ==========================================

@admin.register(Medium)
class MediumAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "school",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "name",
    )

    list_per_page = 25


# ==========================================
# CLASSROOM
# ==========================================

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "school",
        "capacity",
        "floor",
    )

    search_fields = (
        "name",
        "school__name",
    )

    list_filter = (
        "school",
    )

    ordering = (
        "name",
    )

    list_per_page = 25


# ==========================================
# SECTION
# ==========================================

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "class_obj",
        "name",
        "school",
        "stream",
        "sub_stream",
        "medium",
        "classroom",
    )

    search_fields = (
        "name",
        "class_obj__name",
        "school__name",
    )

    list_filter = (
        "school",
        "stream",
        "medium",
        "sub_stream",
    )

    ordering = (
        "class_obj",
        "name",
    )

    list_per_page = 25