from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..resources.student import StudentResource
from ..models.student import StudentAchievement,ExamDetail,Student

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StudentResource
    list_display = (
        'srn',
        'stream',
        'studentclass',
        'section',
        'roll_number',
        'full_name_aadhar',
        'father_full_name_aadhar',
        'mother_full_name_aadhar',
        'date_of_birth',
        'gender',
        'aadhaar_number',
        'category',
        'admission_number',
        'father_mobile',
        'family_id',  # ✅ Added family_id here
        'subjects_opted',
        'subjects',
        'below_poverty_line_certificate_number',
        'religion',
    )

@admin.register(StudentAchievement)
class StudentAchievementAdmin(ImportExportModelAdmin):
    list_display = ("student_name", "achievement_type", "event_name", "rank", "reward_title", "date")
    list_filter = ("achievement_type", "date")
    search_fields = ("student_name", "event_name", "reward_title")

@admin.register(ExamDetail)
class ExamDetailAdmin(ImportExportModelAdmin):
    list_display = ("achievement", "obtained_marks", "total_marks", "percentage")
    search_fields = ("achievement__student_name", "achievement__event_name")