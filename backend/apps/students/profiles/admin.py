from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.students.profiles.models import Student
from apps.students.profiles.student_resource import (
    StudentResource
)


@admin.register(Student)
class StudentAdmin(
    ImportExportModelAdmin
):

    resource_class = StudentResource

    list_display = (
        "srn",
        "full_name_aadhar",

        "student_class",
        "section",
        "roll_number",
        "gender",
        "category",
        "father_mobile",
    )

    search_fields = (
        "srn",
        "full_name_aadhar",
        "aadhaar_number",
        "father_mobile",
    )

    list_filter = (

        "student_class",
        "section",
        "gender",
        "category",
    )

    ordering = (

        "student_class",
        "section",
        "roll_number",
    )

    autocomplete_fields = (

        "student_class",
        "stream",
        "section",
    )

    list_per_page = 25