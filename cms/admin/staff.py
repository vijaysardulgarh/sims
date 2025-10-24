
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..resources.staff import StaffResource,TeacherSubjectAssignmentResource,SanctionedPostResource,ClassInchargeResource,PostTypeResource
from ..models.staff import SanctionedPost,PostType,TeacherAttendance,Staff,TeacherSubjectAssignment,ClassIncharge

@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
                'id',
                'school',
                "employee_id",
                "name",
                "father_name",
                "mother_name",
                "spouse_name",
                "gender",
                "aadhar_number",
                "post_type",
                "category",
                "date_of_birth",
                "joining_date",
                'current_joining_date',
                "retirement_date",
                "qualification",
                "subject",
                "email",
                "mobile_number",
                "staff_role",
                "employment_type",
                "priority",
                "max_periods_per_week"
    )
    list_filter = ("school", "staff_role", "employment_type", "gender", "category")
    search_fields = ("name", "employee_id", "email", "mobile_number")
    ordering = ("priority", "name")  # ✅ staff ordered by priority then name
    resource_class = StaffResource

@admin.register(TeacherSubjectAssignment)
class TeacherSubjectAssignmentAdmin(ImportExportModelAdmin):
    resource_class = TeacherSubjectAssignmentResource

    list_display = (
        "teacher_name",
        "school_name",
        "class_name",
        "section_name",
        "subject_name",
    )
    search_fields = (
        "teacher__name",
        "section__name",
        'section__sec_class__school',
        # "section__school_class__medium__name",
        # "section__school_class__stream__name",
        "class_subject__subject__name",
    )
    list_filter = (
        "teacher",
        "section__sec_class__school",
        # "section__school_class__medium",
        # "section__school_class__stream",
        "section",
        "class_subject__subject",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(teacher__staff_role="Teaching")

    # ---------- Custom display helpers ----------
    def teacher_name(self, obj):
        return obj.teacher.name if obj.teacher else "-"
    teacher_name.short_description = "Teacher"

    def class_name(self, obj):
        return obj.section.sec_class.name if obj.section and obj.section.sec_class else "-"
    class_name.short_description = "Class"

    def section_name(self, obj):
        return obj.section.name if obj.section else "-"
    section_name.short_description = "Section"

    def subject_name(self, obj):
        return obj.class_subject.subject.name if obj.class_subject else "-"
    subject_name.short_description = "Subject"

    def school_name(self, obj):
        return obj.section.sec_class.school.name if obj.section and obj.section.sec_class and obj.section.sec_class.school else "-"
    school_name.short_description = "School"    



@admin.register(SanctionedPost)
class SanctionedPostAdmin(ImportExportModelAdmin):
    list_display = (
        "school",
        "post_type",
        "designation",
        "subject",
        "total_posts",
    )
    list_filter = ("school", "post_type", "subject")
    search_fields = ("designation", "subject__name", "school__name")
    resource_class = SanctionedPostResource    

@admin.register(ClassIncharge)
class ClassInchargeAdmin(ImportExportModelAdmin):
    resource_class = ClassInchargeResource

    list_display = (
        "section",
        "staff",
        "effective_from",
        "effective_to",
        "active",
    )
    list_filter = (
        "active",
        "staff__staff_role",
    )
    search_fields = (
        "section__name",
        "staff__name",
    )
    ordering = ("section",)    

@admin.register(PostType)
class PostTypeAdmin(ImportExportModelAdmin):
    resource_class = PostTypeResource
    list_display = ('name', 'description')
    search_fields = ('name',)    

@admin.register(TeacherAttendance)
class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ("teacher", "date", "present")
    list_editable = ("present",)    




from django import forms
from django.forms import modelformset_factory
class TeacherAttendanceForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = ['teacher', 'present']

# Create a formset for all teachers
TeacherAttendanceFormSet = modelformset_factory(
    TeacherAttendance,
    form=TeacherAttendanceForm,
    extra=0
)    