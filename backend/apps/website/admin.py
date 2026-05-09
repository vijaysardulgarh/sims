from django.contrib import admin
from .models import (
    AboutSchool,
    Principal,
    Affiliation,
    Infrastructure,
    MandatoryPublicDisclosure,
    Facility,
    Event,
    News,
    FAQ,
)


# ==========================================
# ABOUT SCHOOL
# ==========================================

@admin.register(AboutSchool)
class AboutSchoolAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'school',
    )

    search_fields = (
        'school__name',
    )

    ordering = (
        'school',
    )


# ==========================================
# PRINCIPAL
# ==========================================

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
    )

    search_fields = (
        'name',
        'school__name',
    )

    ordering = (
        'name',
    )


# ==========================================
# AFFILIATION
# ==========================================

@admin.register(Affiliation)
class AffiliationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'name',
    )


# ==========================================
# INFRASTRUCTURE
# ==========================================

@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'category',
        'school',
    )

    search_fields = (
        'title',
        'school__name',
    )

    list_filter = (
        'category',
        'school',
    )

    ordering = (
        'category',
        'title',
    )


# ==========================================
# MANDATORY DISCLOSURE
# ==========================================

@admin.register(MandatoryPublicDisclosure)
class MandatoryPublicDisclosureAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'section',
        'school',
        'is_active',
        'order',
    )

    search_fields = (
        'title',
        'school__name',
    )

    list_filter = (
        'section',
        'is_active',
        'school',
    )

    ordering = (
        'section',
        'order',
    )


# ==========================================
# FACILITY
# ==========================================

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'school',
    )

    search_fields = (
        'name',
        'school__name',
    )

    list_filter = (
        'school',
    )

    ordering = (
        'name',
    )


# ==========================================
# EVENT
# ==========================================

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'school',
        'start_date',
        'end_date',
    )

    search_fields = (
        'title',
        'school__name',
        'location',
    )

    list_filter = (
        'school',
        'start_date',
    )

    ordering = (
        '-start_date',
    )


# ==========================================
# NEWS
# ==========================================

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'category',
        'school',
        'date_published',
    )

    search_fields = (
        'title',
        'content',
        'school__name',
    )

    list_filter = (
        'category',
        'school',
        'date_published',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    ordering = (
        '-date_published',
    )


# ==========================================
# FAQ
# ==========================================

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'question',
        'category',
        'school',
        'is_active',
        'order',
    )

    search_fields = (
        'question',
        'answer',
        'school__name',
    )

    list_filter = (
        'category',
        'is_active',
        'school',
    )

    ordering = (
        'order',
        'category',
    )