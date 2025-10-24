from django.contrib import admin



#from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import DateWidget, BooleanWidget,ForeignKeyWidget
import datetime
from django.utils.html import format_html

import logging
# from .models.models import StudentAchievement, ExamDetail
from django.contrib.admin import AdminSite
from import_export.widgets import ForeignKeyWidget,CharWidget
from import_export import widgets
from django.core.exceptions import ValidationError
admin.site.site_header="SIMS" 
admin.site.site_title="SIMS"
admin.site.index_title="School Information Management System"






class ClassWidget(ForeignKeyWidget):
    """
    Custom widget to match Class using School + Class name + Stream + Medium from Excel row.
    """
    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None

        school_name = row.get("School")
        if not school_name:
            raise ValueError("School column is required to identify Class")
        try:
            school = School.objects.get(name=school_name.strip())
        except School.DoesNotExist:
            raise ValueError(f"School '{school_name}' does not exist")

        # Optional Stream and Medium
        stream_name = row.get("Stream")
        medium_name = row.get("Medium")

        classes = Class.objects.filter(school=school, name__iexact=value.strip())

        if stream_name:
            classes = classes.filter(stream__name__iexact=stream_name.strip())
        if medium_name:  # only filter if Medium is provided
            classes = classes.filter(medium__name__iexact=medium_name.strip())


        if not classes.exists():
            raise ValueError(f"Class '{value}' not found in school '{school_name}' with Stream '{stream_name}' and Medium '{medium_name}'")
        if classes.count() > 1:
            raise ValueError(f"Multiple Classes found for '{value}' in '{school_name}' with Stream '{stream_name}' and Medium '{medium_name}'")
        return classes.first()



class ClassInfoWidget(ForeignKeyWidget):
    """
    Custom widget to match Class using School + Class name + Stream + Medium from Excel row.
    """
    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None

        school_name = row.get("School")
        if not school_name:
            raise ValueError("School column is required to identify Class")

        try:
            school = School.objects.get(name=school_name.strip())
        except School.DoesNotExist:
            raise ValueError(f"School '{school_name}' does not exist")

        stream_name = row.get("Stream")
        medium_name = row.get("Medium")

        classes = Class.objects.filter(school=school, name__iexact=value.strip())

        # Stream filter
        if stream_name and stream_name.strip():
            classes = classes.filter(stream__name__iexact=stream_name.strip())
        else:
            classes = classes.filter(stream__isnull=True)

        # Medium filter
        if medium_name and medium_name.strip():
            classes = classes.filter(medium__name__iexact=medium_name.strip())
        else:
            classes = classes.filter(medium__isnull=True)

        if not classes.exists():
            raise ValueError(
                f"Class '{value}' not found in school '{school_name}' with Stream '{stream_name}' and Medium '{medium_name}'"
            )
        if classes.count() > 1:
            raise ValueError(
                f"Multiple Classes found for '{value}' in school '{school_name}' with Stream '{stream_name}' and Medium '{medium_name}'"
            )
        return classes.first()




# from .models.models import TeacherAttendance, Staff
from datetime import date





# admin.site.register(TeacherAttendance, TeacherAttendanceAdmin)    
# admin.site.register(Document,DocumentAdmin)
# #admin.site.register(User)  


# admin.site.register(Facility)
# #admin.site.register(Nodal)
# admin.site.register(Event)
# admin.site.register(News)
# admin.site.register(ExtracurricularActivity)
# admin.site.register(Committee)
# admin.site.register(CommitteeMember)
# admin.site.register(CommitteeMeeting)


# admin.site.register(Stream,StreamAdmin)
# admin.site.register(Class,ClassAdmin)
# admin.site.register(Section,SectionAdmin)
# # admin.site.register(Subject)
# admin.site.register(Staff,StaffAdmin)
# admin.site.register(Classroom,ClassroomAdmin)
# admin.site.register(ClassIncharge,ClassInchargeAdmin)
# admin.site.register(Timetable,TimetableAdmin)
# # admin.site.register(TimetableSlot,TimetableSlotAdmin)
# # admin.site.register(TimetableEntry,TimetableEntryAdmin)
# admin.site.register(Student,StudentAdmin)

# admin.site.register(Book)
# admin.site.register(SMCMember,SMCMemberAdmin)
# admin.site.register(TeacherSubjectAssignment,TeacherSubjectAssignmentAdmin)

from cms.models.school import School
from cms.models.schoolclass import Stream,Medium,Class,Section,Classroom
from cms.models.subject import Subject,ClassSubject
from cms.models.staff import PostType,Staff,TeacherSubjectAssignment,TeacherAttendance
from cms.admin.timetable import Day,Timetable,TimetableSlot

from cms.admin.school import SchoolAdmin
from cms.admin.schoolclass import StreamAdmin,MediumAdmin,ClassAdmin,SectionAdmin,ClassroomAdmin
from cms.admin.subject import SubjectAdmin,ClassSubjectAdmin
from cms.admin.staff import PostTypeAdmin,StaffAdmin,TeacherSubjectAssignmentAdmin,TeacherAttendanceAdmin
from cms.admin.timetable import DayAdmin,TimetableAdmin,TimetableSlotAdmin

class TimetableAdminSite(AdminSite):
    site_header = "Timetable Administration"
    site_title = "Timetable Portal"
    index_title = "Timetable Management"

    def get_app_list(self, request):
        """
        Return a custom-ordered app list, keeping models under one app heading.
        """
        app_list = super().get_app_list(request)

        # Flatten into dict for quick lookup
        app_dict = {app["app_label"]: app for app in app_list}

        # Desired model order (app_label.ModelName)
        model_order = [
            "cms.School",            
            "cms.Stream",
            "cms.Medium",  
            "cms.Class",   
            "cms.Classroom",
            "cms.Section",     
            "cms.Subject",
            "cms.ClassSubject",
            "cms.PostType",
            "cms.Staff",     
            "cms.Day",            
            "cms.TimetableSlot",
            "cms.TeacherSubjectAssignment",
            "cms.Timetable",




        ]

        ordered_apps = []

        for app_label, app in app_dict.items():
            # Build a model lookup
            model_lookup = {m["object_name"]: m for m in app["models"]}

            ordered_models = []
            for model_path in model_order:
                al, model_name = model_path.split(".")
                if al == app_label and model_name in model_lookup:
                    ordered_models.append(model_lookup[model_name])

            # Add any models not in the order list
            for m in app["models"]:
                if m not in ordered_models:
                    ordered_models.append(m)

            # Replace models with ordered list
            app_copy = app.copy()
            app_copy["models"] = ordered_models
            ordered_apps.append(app_copy)

        return ordered_apps


# 👉 This is the object you should import in urls.py
timetable_admin = TimetableAdminSite(name="timetable_admin")

# Register timetable-related models
timetable_admin.register(School,SchoolAdmin)
timetable_admin.register(Stream,StreamAdmin)
timetable_admin.register(Medium,MediumAdmin)
timetable_admin.register(Day,DayAdmin)
timetable_admin.register(TimetableSlot,TimetableSlotAdmin)
timetable_admin.register(Timetable,TimetableAdmin)
timetable_admin.register(Class,ClassAdmin)
timetable_admin.register(Section,SectionAdmin)
timetable_admin.register(Classroom,ClassroomAdmin)
timetable_admin.register(Subject,SubjectAdmin)
timetable_admin.register(ClassSubject,ClassSubjectAdmin)
timetable_admin.register(PostType,PostTypeAdmin)
timetable_admin.register(Staff,StaffAdmin)
timetable_admin.register(TeacherSubjectAssignment,TeacherSubjectAssignmentAdmin)
timetable_admin.register(TeacherAttendance, TeacherAttendanceAdmin)

