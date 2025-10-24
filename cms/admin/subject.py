from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..resources.subject import ClassSubjectResource,SubjectResource
from ..models.subject import Subject,ClassSubject

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    resource_class = SubjectResource    

@admin.register(ClassSubject)
class ClassSubjectAdmin(ImportExportModelAdmin):
    resource_class = ClassSubjectResource

    list_display = (
        "id",
        "school_name",
        "subject_class",
        "stream",
        "sub_stream",
        "subject",
        "theory_periods_per_week",
        "practical_periods_per_week",
        "periods_per_week",
        "is_optional",
        "has_lab",
        "is_shared",
    )
    list_filter = ("subject_class","is_optional", "has_lab", "is_shared")
    search_fields = ("subject_class__name", "stream__name", "subject__name", "subject_class__school__name")
    ordering = ("subject_class", "stream", "subject")

    # Custom method for displaying school
    def school_name(self, obj):
        return obj.subject_class.school.name if obj.subject_class and obj.subject_class.school else "-"
    school_name.admin_order_field = "subject_class__school__name"
    school_name.short_description = "School"    