from django.contrib import admin
from .models import SubjectRequirement

@admin.register(SubjectRequirement)
class SubjectRequirementAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'stream', 'subject', 'theory_periods_per_week', 'lab_periods_per_week')
    list_filter = ('school_class', 'stream')
    search_fields = ('subject__name',)