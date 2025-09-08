from django.contrib import admin
#from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import DateWidget, BooleanWidget,ForeignKeyWidget
import datetime
from django.utils.html import format_html
#from import_export.widgets import DateWidget
#from .models import User
from .models import School
from .models import Affiliation
from .models import Facility
#from .models import Nodal
from .models import Event
from .models import Document
from .models import News
from .models import ExtracurricularActivity
from .models import Committee
from .models import CommitteeMember
from .models import CommitteeMeeting    
from .models import Department
from .models import Stream
from .models import Class
from .models import Section
from .models import Subject
from .models import Staff
from .models import Classroom
from .models import ClassIncharge
from .models import Timetable
from .models import Day,ClassSubject
from .models import TimetableSlot
from .models import TeacherSubjectAssignment,Medium
# from .models import TimetableEntry
from .models import Student,FeeStructure
from .models import PostType,FAQ,MandatoryPublicDisclosure
from .models import Book,Infrastructure,SanctionedPost
from .models import SMCMember,AboutSchool,Principal,Association,AssociationType,AssociationRole,StaffAssociationRoleAssignment
import logging
from .models import StudentAchievement, ExamDetail
from django.contrib.admin import AdminSite
from import_export.widgets import ForeignKeyWidget
admin.site.site_header="SIMS" 
admin.site.site_title="SIMS"
admin.site.index_title="School Information Management System"
class StaffResource(resources.ModelResource):
    school = fields.Field(attribute='school',column_name='School',widget=ForeignKeyWidget(School, field='name'))
    employee_id = fields.Field(attribute='employee_id',column_name='Employee ID')
    name = fields.Field(attribute='name',column_name='Employee Name [ID]')
    father_name = fields.Field(attribute='father_name',column_name="Father's Name")
    mother_name = fields.Field(attribute='mother_name',column_name="Mother's Name")
    spouse_name = fields.Field(attribute='spouse_name',column_name='Spouse Name')
    gender = fields.Field(attribute='gender',column_name='Gender')
    aadhar_number = fields.Field(attribute='aadhar_number',column_name='Aadhar No')
    post_type = fields.Field(attribute='post_type',column_name='Post Type',widget=ForeignKeyWidget(PostType, field='name'))
    category = fields.Field(attribute='category',column_name='Category')
    date_of_birth = fields.Field(attribute='date_of_birth',column_name='Date of Birth')
    joining_date = fields.Field(attribute='joining_date',column_name='Date of Joining Service')
    current_joining_date = fields.Field(attribute='current_joining_date',column_name='Date of Joining Current School')
    retirement_date = fields.Field(attribute='retirement_date',column_name='Retirement Date')
    qualification= fields.Field(attribute='qualification',column_name='Qualification')
    subject = fields.Field(attribute='subject',column_name='Subject',widget=ForeignKeyWidget(Subject, field='name'))
    email = fields.Field(attribute='email',column_name='Email ID')
    mobile_number = fields.Field(attribute='mobile_number',column_name='Mobile Number')
    staff_role = fields.Field(attribute='staff_role',column_name='Staff Role')
    employment_type = fields.Field(attribute='employment_type',column_name='Employment Type')
    #designation = fields.Field(attribute='designation',column_name='Designation')
    priority = fields.Field(attribute='priority', column_name='Priority') 
    class Meta:
        model = Staff
        fields=(
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
                "priority"
                )

    def before_import_row(self, row, **kwargs):
        try:
            if 'Date of Birth' in row and row['Date of Birth']:
                row['Date of Birth'] = self.reformat_date(row['Date of Birth'])
            if 'Date of Joining School/Office' in row and row['Date of Joining School/Office']:
                row['Date of Joining School/Office'] = self.reformat_date(row['Date of Joining School/Office'])
        except ValueError as e:
            logging.error(f"Error converting date: {e}. Row: {row}")

    def reformat_date(self, date_str):
        try:
            original_format = "%Y-%m-%d"  # Adjust format for date with time
            date_obj = datetime.datetime.strptime(date_str, original_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error parsing date '{date_str}': {e}")
            return None  # Or provide a default value
        
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
                "priority"
    )
    list_filter = ("school", "staff_role", "employment_type", "gender", "category")
    search_fields = ("name", "employee_id", "email", "mobile_number")
    ordering = ("priority", "name")  # ✅ staff ordered by priority then name
    resource_class = StaffResource

class StudentResource(resources.ModelResource):

   
    srn = fields.Field(attribute='srn', column_name='SRN')
    school_code = fields.Field(attribute='school_code', column_name='SchoolCode')
    school_name = fields.Field(attribute='school_name', column_name='SchoolName')
    admission_date = fields.Field(attribute='admission_date', column_name='Admission Date')
    studentclass = fields.Field(attribute='studentclass', column_name='Class')
    stream = fields.Field(attribute='stream', column_name='Stream')
    section = fields.Field(attribute='section', column_name='Section')
    roll_number = fields.Field(attribute='roll_number', column_name='Roll Number')
    admission_number = fields.Field(attribute='admission_number', column_name='Admission Number')
 
    # Personal Info

    full_name_aadhar = fields.Field(attribute='full_name_aadhar', column_name='FullName as on Aadhar Card')
    # name_in_local_language = fields.Field(attribute='name_in_local_language', column_name='Name In Local Language')
    date_of_birth = fields.Field(attribute='date_of_birth', column_name='Date of Birth')
    gender = fields.Field(attribute='gender', column_name='Gender')
    aadhaar_number = fields.Field(attribute='aadhaar_number', column_name='Aadhaar Number (If any)')
    domicile_of_haryana = fields.Field(attribute='domicile_of_haryana', column_name='Domicile Of Haryana?')

    # Parents / Guardian

    father_full_name_aadhar = fields.Field(attribute='father_full_name_aadhar', column_name="Father's Full Name aso on Aadhar Card")
    father_aadhaar_number = fields.Field(attribute='father_aadhaar_number', column_name="Father's Aadhaar Number")
    mother_full_name_aadhar = fields.Field(attribute='mother_full_name_aadhar', column_name="Mother's Full Name as on Aadhaar")
    mother_aadhaar_number = fields.Field(attribute='mother_aadhaar_number', column_name="Mother's Aadhaar Number")

    # Contact

    father_mobile = fields.Field(attribute='father_mobile', column_name="Father's Mobile No")
    mother_mobile = fields.Field(attribute='mother_mobile', column_name="Mother's Mobile No")

    # Financial
    family_annual_income = fields.Field(attribute='family_annual_income', column_name='Family Annual Income')
    account_number = fields.Field(attribute='account_number', column_name='Account Number')
    bank_name = fields.Field(attribute='bank_name', column_name='Bank Name')
    ifsc = fields.Field(attribute='ifsc', column_name='IFSC')

    # Subjects
    subjects_opted = fields.Field(attribute='subjects_opted', column_name='Subjects opted by student')
    subjects = fields.Field(attribute='subjects', column_name='Processed Subjects')  # ✅ your cleaned subjects logic

    caste = fields.Field(attribute='caste', column_name='Caste Name')
    category = fields.Field(attribute='category', column_name='Category Name')
    disability = fields.Field(attribute='disability', column_name='Disability')
    disorder = fields.Field(attribute='disorder', column_name='Disorder Name')
    bpl_certificate_issuing_authority = fields.Field(attribute='bpl_certificate_issuing_authority', column_name='BPL Certificate Issuing Authority')
    below_poverty_line_certificate_number = fields.Field(attribute='below_poverty_line_certificate_number', column_name='Below Poverty Line Certificate Number')
    
    family_id = fields.Field(attribute='family_id', column_name='FamilyId') 

    class Meta:
        model = Student
        import_id_fields = ['srn']
        export_order = ( 
            'srn', 
            'school_code', 
            'school_name', 
            'admission_date',
            'studentclass', 
            'stream', 
            'section', 
            'roll_number', 
            'admission_number',

            # Personal Info
             'full_name_aadhar', 
            # 'name_in_local_language',
             'date_of_birth', 
             'gender', 
             'aadhaar_number', 
             'domicile_of_haryana', 

            # Parents / Guardian
            'father_full_name_aadhar', 
            'father_aadhaar_number', 
            'mother_full_name_aadhar', 
            'mother_aadhaar_number',

            # Contact
            'father_mobile',
            'mother_mobile',

            # Financial
            'family_annual_income', 
            'account_number',
            'bank_name',
            'ifsc',

            # Subjects
             'subjects_opted', 
             'subjects',

             'caste',
             'category',
             'disability',
             'disorder',
             'bpl_certificate_issuing_authority',
             'below_poverty_line_certificate_number',
             'family_id'
             
        )
      
    def before_import(self, dataset, **kwargs):
    # Collect all SRNs from the Excel file
        excel_srn_list = [row['SRN'] for row in dataset.dict]

        # Get all existing SRNs from the database
        existing_srn_set = set(Student.objects.values_list('srn', flat=True))

        # Find SRNs that need to be deleted
        srns_to_delete = existing_srn_set - set(excel_srn_list)

        # Delete records from the database whose SRNs are not present in the Excel file
        if srns_to_delete:
            Student.objects.filter(srn__in=srns_to_delete).delete()
            
    def before_import_row(self, row, **kwargs):
        try:
            if 'Date of Birth' in row and row['Date of Birth']:
                row['Date of Birth'] = self.reformat_date(row['Date of Birth'])
            if 'Admission Date' in row and row['Admission Date']:
                row['Admission Date'] = self.reformat_date(row['Admission Date'])
        except ValueError as e:
            logging.error(f"Error converting date: {e}. Row: {row}")

    def reformat_date(self, date_str):
        try:
            original_format = "%b %d, %Y"  # Adjust format for date with time
            date_obj = datetime.datetime.strptime(date_str, original_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error parsing date '{date_str}': {e}")
            return None  # Or provide a default value
        
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
    )



# --- Widgets ---



# class ClassWidget(ForeignKeyWidget):
#     def __init__(self):
#         super().__init__(Class, "name")

#     def clean(self, value, row=None, *args, **kwargs):
#         if not value:
#             return None

#         school_name = row.get("School")
#         if not school_name:
#             raise ValueError("School column is required to identify Class")

#         try:
#             school = School.objects.get(name=school_name.strip())
#         except School.DoesNotExist:
#             raise ValueError(f"School '{school_name}' does not exist")

#         stream_name = row.get("Stream")
#         medium_name = row.get("Medium")

#         classes = Class.objects.filter(
#             school=school,
#             name__iexact=value.strip()
#         )
#         if stream_name:
#             classes = classes.filter(stream__name__iexact=stream_name.strip())
#         if medium_name:
#             classes = classes.filter(medium__name__iexact=medium_name.strip())

#         if not classes.exists():
#             raise ValueError(
#                 f"Class '{value}' not found in School '{school_name}' "
#                 f"with Stream '{stream_name}' and Medium '{medium_name}'"
#             )
#         if classes.count() > 1:
#             raise ValueError(
#                 f"Multiple Classes found for '{value}' in School '{school_name}' "
#                 f"with Stream '{stream_name}' and Medium '{medium_name}'"
#             )

#         return classes.first()


# class SubjectWidget(ForeignKeyWidget):
#     def __init__(self):
#         super().__init__(Subject, "name")

#     def clean(self, value, row=None, *args, **kwargs):
#         if not value:
#             return None
#         try:
#             return Subject.objects.get(name=value.strip())
#         except Subject.DoesNotExist:
#             raise ValueError(f"Subject '{value}' does not exist")


# class ClassSubjectWidget(ForeignKeyWidget):
#     def __init__(self):
#         super().__init__(ClassSubject, "id")  # Ensure correct call to parent constructor

#     def clean(self, value, row=None, *args, **kwargs):
#         class_name = row.get("Class Name")
#         subject_name = row.get("Subject")

#         if not class_name or not subject_name:
#             raise ValueError("Both 'Class Name' and 'Subject' are required")

#         class_obj = ClassWidget().clean(class_name, row=row)
#         subject_obj = SubjectWidget().clean(subject_name, row=row)

#         try:
#             return ClassSubject.objects.get(
#                 class_info=class_obj,
#                 subject=subject_obj
#             )
#         except ClassSubject.DoesNotExist:
#             raise ValueError(
#                 f"ClassSubject not found for Class '{class_name}' and Subject '{subject_name}'"
#             )
# --- Teacher Subject Assignment Resource ---

class TeacherSubjectAssignmentResource(resources.ModelResource):
    # Raw FK fields with widgets
    teacher = fields.Field(
        column_name="teacher",
        attribute="teacher",
        widget=ForeignKeyWidget(Staff, "id")   # import by Staff.id
    )
    class_subject = fields.Field(
        column_name="class_subject",
        attribute="class_subject",
        widget=ForeignKeyWidget(ClassSubject, "id")   # import by ClassSubject.id
    )

    # Human-readable Excel fields
    teacher_name = fields.Field(column_name="Teacher")
    school_name = fields.Field(column_name="School")
    class_name = fields.Field(column_name="Class")
    stream_name = fields.Field(column_name="Stream")
    medium_name = fields.Field(column_name="Medium")
    subject_name = fields.Field(column_name="Subject")
    max_periods_per_week = fields.Field(
        column_name="Max Periods / Week",
        attribute="max_periods_per_week"
    )

    class Meta:
        model = TeacherSubjectAssignment
        import_id_fields = ("teacher", "class_subject")
        fields = (
            "id",
            "teacher",
            "class_subject",
            "teacher_name",
            "school_name",
            "class_name",
            "stream_name",
            "medium_name",
            "subject_name",
            "max_periods_per_week",
        )
        export_order = fields

    # --- EXPORT (Readable) ---
    def dehydrate_teacher_name(self, obj):
        return obj.teacher.name if obj.teacher else ""

    def dehydrate_subject_name(self, obj):
        return obj.class_subject.subject.name if obj.class_subject and obj.class_subject.subject else ""

    def dehydrate_class_name(self, obj):
        return obj.class_subject.class_info.name if obj.class_subject and obj.class_subject.class_info else ""

    def dehydrate_school_name(self, obj):
        return (
            obj.class_subject.class_info.school.name
            if obj.class_subject and obj.class_subject.class_info and obj.class_subject.class_info.school
            else ""
        )

    def dehydrate_stream_name(self, obj):
        return (
            obj.class_subject.class_info.stream.name
            if obj.class_subject and obj.class_subject.class_info and obj.class_subject.class_info.stream
            else ""
        )

    def dehydrate_medium_name(self, obj):
        return (
            obj.class_subject.class_info.medium.name
            if obj.class_subject and obj.class_subject.class_info and obj.class_subject.class_info.medium
            else ""
        )

    # --- IMPORT (Smart lookup) ---
    def before_import_row(self, row, **kwargs):
        teacher_name = row.get("Teacher")
        school_name = row.get("School")
        class_name = row.get("Class")
        stream_name = row.get("Stream")
        medium_name = row.get("Medium")
        subject_name = row.get("Subject")

        # Teacher lookup
        teacher = Staff.objects.filter(name=teacher_name, staff_role="Teaching").first()
        if not teacher:
            raise Exception(f"Teacher '{teacher_name}' not found.")

        # Class lookup
        class_qs = Class.objects.filter(
            name=class_name,
            school__name=school_name,
            stream__name=stream_name,
            medium__name=medium_name,
        )
        if not class_qs.exists():
            raise Exception(
                f"Class '{class_name}' with School='{school_name}', Stream='{stream_name}', Medium='{medium_name}' not found."
            )
        class_obj = class_qs.first()

        # Subject lookup
        subject = Subject.objects.filter(name=subject_name).first()
        if not subject:
            raise Exception(f"Subject '{subject_name}' not found.")

        # ClassSubject lookup
        class_subject = ClassSubject.objects.filter(
            class_info=class_obj,
            subject=subject
        ).first()
        if not class_subject:
            raise Exception(
                f"ClassSubject for Class='{class_name}' and Subject='{subject_name}' not found."
            )

        # ✅ Instead of PKs, assign the **actual instance**
        row["teacher"] = teacher.id
        row["class_subject"] = class_subject.id


class TeacherSubjectAssignmentAdmin(ImportExportModelAdmin):
    resource_class = TeacherSubjectAssignmentResource

    list_display = (
        "teacher_name",
        "class_name",
        "subject_name",
        "max_periods_per_week",
    )
    search_fields = (
        "teacher__name",
        "class_subject__class_info__name",
        "class_subject__class_info__medium__name",
        "class_subject__class_info__stream__name",
        "class_subject__subject__name",
    )
    list_filter = (
        "teacher",
        "class_subject__class_info__medium",
        "class_subject__class_info__stream",
        "class_subject__class_info",
        "class_subject__subject",
    )

    def get_queryset(self, request):
        # Limit queryset to only Teaching staff
        qs = super().get_queryset(request)
        return qs.filter(teacher__staff_role="Teaching")

    # Custom column for Teacher
    def teacher_name(self, obj):
        return obj.teacher.name if obj.teacher else "-"
    teacher_name.short_description = "Teacher"

    # Custom column for Class
    def class_name(self, obj):
        return obj.class_subject.class_info.name if obj.class_subject else "-"
    class_name.short_description = "Class"

    # Custom column for Subject
    def subject_name(self, obj):
        return obj.class_subject.subject.name if obj.class_subject else "-"
    subject_name.short_description = "Subject"

# -------------------
# Day Resource & Admin
# -------------------
class DayResource(resources.ModelResource):
    class Meta:
        model = Day
        fields = ("id", "school__name", "name", "sequence")
        export_order = ("id", "school__name", "name", "sequence")

@admin.register(Day)
class DayAdmin(ImportExportModelAdmin):
    resource_class = DayResource
    list_display = ("id", "school", "name", "sequence")
    search_fields = ("name", "school__name")
    list_filter = ("school",)
    ordering = ("school", "sequence")

# -------------------
# TimetableSlot Resource & Admin
# -------------------
class SchoolWidget(ForeignKeyWidget):
    def __init__(self):
        super().__init__(School, "name")


class DayWidget(ForeignKeyWidget):
    """Custom Day widget that also considers school"""
    def __init__(self):
        super().__init__(Day, "name")

    def clean(self, value, row=None, *args, **kwargs):
        school_name = row.get("School")  # get school from import row
        if not school_name:
            return None
        try:
            school = School.objects.get(name=school_name)
            return Day.objects.get(school=school, name=value)
        except (School.DoesNotExist, Day.DoesNotExist):
            raise ValueError(f"Day '{value}' not found for school '{school_name}'")


class TimetableSlotResource(resources.ModelResource):
    
    school = fields.Field(
        column_name="School",
        attribute="school",
        widget=SchoolWidget()   # ✅ model class, not string
    )
    day = fields.Field(
        column_name="Day",
        attribute="day",
        widget=DayWidget()      # ✅ model class, not string
    )

    class Meta:
        model = TimetableSlot
        fields = (
            "id",
            "school",
            "day",
            "sequence_number",
            "period_number",
            "start_time",
            "end_time",
            "is_break",
            "is_assembly",
            "is_special_event",
        )
        export_order = fields
        import_id_fields = ("school", "day", "sequence_number")

@admin.register(TimetableSlot)
class TimetableSlotAdmin(ImportExportModelAdmin):
    resource_class = TimetableSlotResource
    list_display = (
        "school",
        "day",
        "sequence_number",
        "period_number",
        "start_time",
        "end_time",
        "is_break",
        "is_assembly",
        "is_special_event",
    )
    list_filter = ("school", "day", "is_break", "is_assembly", "is_special_event")
    ordering = ("school", "day__sequence", "sequence_number")

# -------------------
# Medium Resource
# -------------------
class MediumResource(resources.ModelResource):
    school = fields.Field(
        column_name="School",
        attribute="school",
        widget=ForeignKeyWidget(School, "name")  # use school.name instead of ID
    )
    name = fields.Field(column_name="Medium Name", attribute="name")

    class Meta:
        model = Medium
        fields = ("id", "name", "school")
        export_order = ("id", "school", "name")
        import_id_fields = ("school", "name")  # respects unique_together


# -------------------
# Medium Admin
# -------------------
@admin.register(Medium)
class MediumAdmin(ImportExportModelAdmin):
    resource_class = MediumResource
    list_display = ("name", "school")
    search_fields = ("name", "school__name")
    list_filter = ("school",)

class TimetableEntryResource(resources.ModelResource):
    section = fields.Field(attribute='section',column_name='Section')
    subject = fields.Field(attribute='subject',column_name='Subject')
    teacher = fields.Field(attribute='teacher',column_name='Teacher')
    slot = fields.Field(attribute='slot',column_name='Slot')

    class Meta:
        model = Timetable
        fields=('section','subject','teacher','slot')
        #use_id=False

class TimetableEntryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('section','subject','teacher','slot')
    resource_class=TimetableEntryResource    

# --- ClassSubject Widget ---
class ClassSubjectWidget(ForeignKeyWidget):
    def __init__(self, model, field, *args, **kwargs):
        super().__init__(model, field, *args, **kwargs)

    def clean(self, value, row=None, *args, **kwargs):
        class_name = row.get("Class Name")
        subject_name = row.get("Subject")

        if not class_name or not subject_name:
            raise ValueError("Both 'Class Name' and 'Subject' are required")

        try:
            class_obj = Class.objects.get(name=class_name.strip())
            subject_obj = Subject.objects.get(name=subject_name.strip())
            return ClassSubject.objects.get(class_info=class_obj, subject=subject_obj)
        except (Class.DoesNotExist, Subject.DoesNotExist, ClassSubject.DoesNotExist):
            raise ValueError(f"ClassSubject not found for Class '{class_name}' and Subject '{subject_name}'")


# --- TimetableSlot Widget ---
class TimetableSlotWidget(ForeignKeyWidget):
    def __init__(self, model, field, *args, **kwargs):
        super().__init__(model, field, *args, **kwargs)

    def clean(self, value, row=None, *args, **kwargs):
        school_name = row.get("School")
        day_name = row.get("Day")
        sequence_number = row.get("Sequence Number")

        if not (school_name and day_name and sequence_number):
            raise ValueError("School, Day, and Sequence Number are required to identify TimetableSlot")

        try:
            school = School.objects.get(name=school_name.strip())
            day = school.day_set.get(name=day_name.strip())  # Assuming Day FK to School
            return TimetableSlot.objects.get(
                school=school,
                day=day,
                sequence_number=int(sequence_number)
            )
        except (School.DoesNotExist, Day.DoesNotExist, TimetableSlot.DoesNotExist):
            raise ValueError(f"TimetableSlot not found for given identifiers")
# -------------------
# Timetable Resource & Admin
# -------------------
class TimetableResource(resources.ModelResource):
    school = fields.Field(
        column_name="School",
        attribute="school",
        widget=ForeignKeyWidget(School, "name")
    )
    section = fields.Field(
        column_name="Section",
        attribute="section",
        widget=ForeignKeyWidget(Section, "name")
    )
    class_subject = fields.Field(
        column_name="Class Subject",
        attribute="class_subject",
        widget=ClassSubjectWidget(ClassSubject, "id")
    )
    teacher = fields.Field(
        column_name="Teacher",
        attribute="teacher",
        widget=ForeignKeyWidget(Staff, "name")
    )
    slot = fields.Field(
        column_name="Slot",
        attribute="slot",
        widget=TimetableSlotWidget(TimetableSlot, "id")
    )
    classroom = fields.Field(
        column_name="Classroom",
        attribute="classroom",
        widget=ForeignKeyWidget(Classroom, "name")
    )
    substitute_teacher = fields.Field(
        column_name="Substitute Teacher",
        attribute="substitute_teacher",
        widget=ForeignKeyWidget(Staff, "name")
    )

    class Meta:
        model = Timetable
        fields = (
            "id",
            "school",
            "section",
            "class_subject",
            "teacher",
            "slot",
            "classroom",
            "substitute_teacher",
        )
        export_order = fields
        import_id_fields = ("section", "slot", "teacher")




class TimetableAdmin(ImportExportModelAdmin):
    resource_class = TimetableResource
    list_display = (
        "school",
        "section",
        "get_class",
        "get_subject",
        "teacher",
        "slot",
        "classroom",
        "substitute_teacher",
    )
    search_fields = (
        "school__name",
        "section__name",
        "class_subject__class_info__name",
        "class_subject__subject__name",
        "teacher__name",
    )
    list_filter = ("school", "section", "teacher", "slot__day")

    def get_class(self, obj):
        return obj.class_subject.class_info
    get_class.short_description = "Class"

    def get_subject(self, obj):
        return obj.class_subject.subject
    get_subject.short_description = "Subject"

class SMCMemberResource(resources.ModelResource):
    school = fields.Field(
        attribute='school',
        column_name='School',
        widget=ForeignKeyWidget(School, field='name')
    )
    name = fields.Field(attribute='name', column_name='Member Name')
    position = fields.Field(attribute='position', column_name='Position')
    gender = fields.Field(attribute='gender', column_name='Gender')
    category = fields.Field(attribute='category', column_name='Category')
    contact_number = fields.Field(attribute='contact_number', column_name='Contact Number')
    email = fields.Field(attribute='email', column_name='Email')
    remarks = fields.Field(attribute='remarks', column_name='Remarks')
    priority = fields.Field(attribute='priority', column_name='Priority')  # 🔹 Added priority field

    class Meta:
        model = SMCMember
        fields = (
            "id",
            "school",
            "name",
            "position",
            "gender",
            "category",
            "contact_number",
            "email",
            "remarks",
            "priority",   # 🔹 include priority in export
        )
        export_order = (
            "id",
            "school",
            "name",
            "position",
            "gender",
            "category",
            "contact_number",
            "email",
            "remarks",
            "priority",   # 🔹 ensure consistent order
        )


class SMCMemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'position', 'gender', 'category', 'contact_number', 'email', "school", 'priority', 'photo_tag')
    list_filter = ("position", "gender", "category", "school")
    search_fields = ("name", "email", "contact_number")
    resource_class = SMCMemberResource

    # 🔹 Photo preview in admin
    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.photo.url
            )
        return "No Photo"
    photo_tag.short_description = "Photo"


class SanctionedPostResource(resources.ModelResource):
    school = fields.Field(
        attribute='school',
        column_name='School',
        widget=ForeignKeyWidget(School, field='name')
    )
    subject = fields.Field(
        attribute='subject',
        column_name='Subject',
        widget=ForeignKeyWidget(Subject, field='name')
    )

    post_type = fields.Field(attribute='post_type',column_name='Post Type',widget=ForeignKeyWidget(PostType, field='name'))
    designation = fields.Field(attribute='designation', column_name='Designation')
    total_posts = fields.Field(attribute='total_posts', column_name='Total Posts')

    class Meta:
        model = SanctionedPost
        fields = (
            "id",
            "school",
            "post_type",
            "designation",
            "subject",
            "total_posts",
        )
        export_order = (
            "id",
            "school",
            "post_type",
            "designation",
            "subject",
            "total_posts",
        )


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "school", "uploaded_at")
    search_fields = ("title", "school__name")

class StaffAssociationRoleAssignmentInline(admin.TabularInline):
    model = StaffAssociationRoleAssignment
    extra = 1   # number of empty forms displayed
    autocomplete_fields = ["role", "staff"]  # improves usability if you have many records
    show_change_link = True


# @admin.register(Staff)
# class StaffAdmin(admin.ModelAdmin):
#     list_display = ("name", "employee_id", "school", "designation", "staff_role")
#     list_filter = ("school", "staff_role", "employment_type", "category")
#     search_fields = ("name", "employee_id", "email", "mobile_number")
#     inlines = [StaffAssociationRoleAssignmentInline]   # ✅ roles inline inside staff profile

class AssociationTypeResource(resources.ModelResource):
    name = fields.Field(attribute="name", column_name="Type")

    class Meta:
        model = AssociationType
        fields = ("id", "name")
        export_order = ("id", "name")


class AssociationResource(resources.ModelResource):
    type = fields.Field(
        attribute="type",
        column_name="Type",
        widget=ForeignKeyWidget(AssociationType, field="name"),
    )
    school = fields.Field(
        attribute="school",
        column_name="School",
        widget=ForeignKeyWidget(School, field="name"),
    )

    class Meta:
        model = Association
        fields = ("id", "name", "type", "school")
        export_order = ("id", "name", "type", "school")


class AssociationRoleResource(resources.ModelResource):
    association = fields.Field(
        attribute="association",
        column_name="Association",
        widget=ForeignKeyWidget(Association, field="name"),
    )

    class Meta:
        model = AssociationRole
        fields = ("id", "title", "responsibilities", "association")
        export_order = ("id", "title", "responsibilities", "association")


class StaffAssociationRoleAssignmentResource(resources.ModelResource):
    staff = fields.Field(
        attribute="staff",
        column_name="Staff",
        widget=ForeignKeyWidget(Staff, field="name"),
    )
    role = fields.Field(
        attribute="role",
        column_name="Role",
        widget=ForeignKeyWidget(AssociationRole, field="title"),
    )

    class Meta:
        model = StaffAssociationRoleAssignment
        fields = ("id", "staff", "role", "assigned_on")
        export_order = ("id", "staff", "role", "assigned_on")

@admin.register(AssociationType)
class AssociationTypeAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    resource_class = AssociationTypeResource


@admin.register(Association)
class AssociationAdmin(ImportExportModelAdmin):
    list_display = ("name", "type", "school")
    list_filter = ("type", "school")
    search_fields = ("name", "school__name")
    resource_class = AssociationResource


@admin.register(AssociationRole)
class AssociationRoleAdmin(ImportExportModelAdmin):
    list_display = ("title", "association")
    list_filter = ("association",)
    search_fields = ("title", "association__name")
    resource_class = AssociationRoleResource


@admin.register(StaffAssociationRoleAssignment)
class StaffAssociationRoleAssignmentAdmin(ImportExportModelAdmin):
    list_display = ("staff", "role", "assigned_on")
    list_filter = ("role__association__type", "role__association__school")
    search_fields = ("staff__name", "role__title", "role__association__name")
    resource_class = StaffAssociationRoleAssignmentResource


class InfrastructureResource(resources.ModelResource):
    school = fields.Field(
        attribute="school",
        column_name="School",
        widget=ForeignKeyWidget(School, field="name"),
    )
    title = fields.Field(attribute="title", column_name="Title")
    description = fields.Field(attribute="description", column_name="Description")
    category = fields.Field(attribute="category", column_name="Category")

    class Meta:
        model = Infrastructure
        fields = ("id", "school", "title", "description", "category")
        export_order = ("id", "school", "title", "description", "category")    

@admin.register(Infrastructure)
class InfrastructureAdmin(ImportExportModelAdmin):
    list_display = ("title", "school", "category", "photo_tag")
    list_filter = ("category", "school")
    search_fields = ("title", "school__name", "description")
    resource_class = InfrastructureResource

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="70" height="50" style="object-fit:cover;border-radius:4px;"/>',
                obj.photo.url,
            )
        return "-"
    photo_tag.short_description = "Photo"

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


class AboutSchoolResource(resources.ModelResource):
    school = fields.Field(
        attribute="school",
        column_name="School",
        widget=ForeignKeyWidget(School, field="name"),
    )

    class Meta:
        model = AboutSchool
        fields = ("id", "school", "history", "vision", "mission")
        export_order = ("id", "school", "history", "vision", "mission")


class PrincipalResource(resources.ModelResource):
    school = fields.Field(
        attribute="school",
        column_name="School",
        widget=ForeignKeyWidget(School, field="name"),
    )

    class Meta:
        model = Principal
        fields = ("id", "school", "name", "message")
        export_order = ("id", "school", "name", "message")


class AffiliationResource(resources.ModelResource):
    school = fields.Field(
        attribute="school",
        column_name="School",
        widget=ForeignKeyWidget(School, field="name"),
    )

    class Meta:
        model = Affiliation
        fields = ("id", "school", "name", "description")
        export_order = ("id", "school", "name", "description")


@admin.register(AboutSchool)
class AboutSchoolAdmin(ImportExportModelAdmin):
    list_display = ("school", "short_history", "short_vision", "short_mission")
    search_fields = ("school__name", "history", "vision", "mission")
    resource_class = AboutSchoolResource

    def short_history(self, obj):
        return (obj.history[:50] + "...") if obj.history else "-"
    short_history.short_description = "History"

    def short_vision(self, obj):
        return (obj.vision[:50] + "...") if obj.vision else "-"
    short_vision.short_description = "Vision"

    def short_mission(self, obj):
        return (obj.mission[:50] + "...") if obj.mission else "-"
    short_mission.short_description = "Mission"


@admin.register(Principal)
class PrincipalAdmin(ImportExportModelAdmin):
    list_display = ("name", "school", "photo_tag", "short_message")
    search_fields = ("name", "school__name", "message")
    resource_class = PrincipalResource

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:50%;"/>',
                obj.photo.url,
            )
        return "-"
    photo_tag.short_description = "Photo"

    def short_message(self, obj):
        return (obj.message[:60] + "...") if obj.message else "-"
    short_message.short_description = "Message"


@admin.register(Affiliation)
class AffiliationAdmin(ImportExportModelAdmin):
    list_display = ("name", "school", "short_description")
    search_fields = ("name", "school__name", "description")
    resource_class = AffiliationResource

    def short_description(self, obj):
        return (obj.description[:60] + "...") if obj.description else "-"
    short_description.short_description = "Description"


class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject
        fields = ("id", "name")
        export_order = ("id", "name")

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    resource_class = SubjectResource        


# Step 1: Define resource
class SchoolResource(resources.ModelResource):
    class Meta:
        model = School
        fields = (
            "id",
            "name",
            "address",
            "website",
            "email",
            "phone_number",
            "logo",
            "accreditation",
            "established_date",
            "motto",
            "social_media_links",
        )
        export_order = fields  # keep same order when exporting

# Step 2: Register with ImportExportModelAdmin
@admin.register(School)
class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource
    list_display = ("name", "email", "phone_number", "established_date")
    search_fields = ("name", "email", "phone_number")
    list_filter = ("established_date", "accreditation")


class PostTypeResource(resources.ModelResource):
    class Meta:
        model = PostType
        fields = ('id', 'name', 'description')  # specify fields for import/export
        export_order = ('id', 'name', 'description')

# Admin with import/export support
@admin.register(PostType)
class PostTypeAdmin(ImportExportModelAdmin):
    resource_class = PostTypeResource
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(StudentAchievement)
class StudentAchievementAdmin(ImportExportModelAdmin):
    list_display = ("student_name", "achievement_type", "event_name", "rank", "reward_title", "date")
    list_filter = ("achievement_type", "date")
    search_fields = ("student_name", "event_name", "reward_title")

@admin.register(ExamDetail)
class ExamDetailAdmin(ImportExportModelAdmin):
    list_display = ("achievement", "obtained_marks", "total_marks", "percentage")
    search_fields = ("achievement__student_name", "achievement__event_name")


@admin.register(FeeStructure)
class FeeStructureAdmin(ImportExportModelAdmin):
    list_display = (
        "student_class",
        "stream",
        "admission_fee_display",
        "rcf_display",
        "cwf_display",
        "ccwf_display",
        "total_fee_display",
    )
    search_fields = ("student_class__name", "stream__name")
    list_filter = ("student_class", "stream")

    def admission_fee_display(self, obj):
        return round(obj.admission_fee)
    admission_fee_display.short_description = "Admission Fee"

    def rcf_display(self, obj):
        return round(obj.rcf)
    rcf_display.short_description = "RCF"

    def cwf_display(self, obj):
        return round(obj.cwf)
    cwf_display.short_description = "CWF"

    def ccwf_display(self, obj):
        return round(obj.ccwf)
    ccwf_display.short_description = "CCWF"

    def total_fee_display(self, obj):
        return round(obj.total_fee())
    total_fee_display.short_description = "Total Fee"


# --- Import/Export Resource ---
class FAQResource(resources.ModelResource):
    class Meta:
        model = FAQ
        fields = ("id", "question", "answer", "category", "order", "is_active", "created_at", "updated_at")
        export_order = ("id", "question", "answer", "category", "order", "is_active", "created_at", "updated_at")


# --- Admin Registration ---
@admin.register(FAQ)
class FAQAdmin(ImportExportModelAdmin):  # inherit ImportExportModelAdmin
    resource_class = FAQResource

    list_display = ("question", "category", "is_active", "order", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("question", "answer")
    ordering = ("order", "category")
    list_editable = ("is_active", "order")

    fieldsets = (
        (None, {
            "fields": ("question", "answer", "category", "order", "is_active")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    # Auto-populate order if not set
    def save_model(self, request, obj, form, change):
        if not obj.order:  # if order not set
            max_order = FAQ.objects.filter(category=obj.category).aggregate(admin.models.Max("order"))["order__max"]
            obj.order = (max_order or 0) + 1
        super().save_model(request, obj, form, change)

@admin.register(MandatoryPublicDisclosure)
class MandatoryPublicDisclosureAdmin(ImportExportModelAdmin):
    list_display = ("section", "title", "value", "file", "order", "is_active")
    list_filter = ("section", "is_active")
    search_fields = ("title", "value")
    ordering = ("section", "order")


class StreamResource(resources.ModelResource):
    stream_name = fields.Field(
        column_name='Stream Name',
        attribute='name'
    )
    school_name = fields.Field(
        column_name='School Name'
    )

    class Meta:
        model = Stream
        fields = ('id', 'stream_name', 'school_name')
        export_order = ('id', 'stream_name', 'school_name')
        import_id_fields = ('id',)

    def before_import_row(self, row, **kwargs):
        school_name = row.get('School Name')
        try:
            school = School.objects.get(name=school_name)
            row['school'] = school.id  # Convert name → ID before import
        except School.DoesNotExist:
            row['school'] = None  # Or raise a validation error

    def dehydrate_school_name(self, stream):
        # For exporting: show school name instead of ID
        return stream.school.name if stream.school else ""

    def hydrate_school_name(self, value):
        # Used during import: map school name to school instance
        try:
            return School.objects.get(name=value)
        except School.DoesNotExist:
            return None

class StreamAdmin(ImportExportModelAdmin):
    resource_class = StreamResource
    list_display = ('name', 'school')
    search_fields = ('name', 'school__name')

class ClassroomResource(resources.ModelResource):
    class Meta:
        model = Classroom
        fields = (
            "id",
            "school__name",
            "room_number",
            "capacity",
            "floor",
        )
        export_order = fields


class ClassResource(resources.ModelResource):
    school = fields.Field(
        column_name="School",       # must match column in Excel/CSV
        attribute="school",
        widget=ForeignKeyWidget(School, "name")   # match by School.name
    )
    stream = fields.Field(
        column_name="Stream",
        attribute="stream",
        widget=ForeignKeyWidget(Stream, "name")
    )
    medium = fields.Field(
        column_name="Medium",
        attribute="medium",
        widget=ForeignKeyWidget(Medium, "name")
    )

    class Meta:
        model = Class
        fields = ("id", "school", "name", "stream", "medium")
        export_order = ("id", "school", "name", "stream", "medium")


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


class SectionResource(resources.ModelResource):
    school = fields.Field(column_name="School", attribute="school_class", readonly=True)
    school_class = fields.Field(column_name="Class", attribute="school_class", widget=ClassWidget(Class, "name"))
    stream = fields.Field(column_name="Stream", readonly=True)
    medium = fields.Field(column_name="Medium", readonly=True)
    section_name = fields.Field(column_name="Section Name", attribute="name")
    classroom_number = fields.Field(column_name="Classroom", attribute="classroom", widget=ForeignKeyWidget(Classroom, "room_number"))

    class Meta:
        model = Section
        fields = ("id", "school", "school_class", "stream", "medium", "section_name", "classroom_number")
        export_order = ("id", "school", "school_class", "stream", "medium", "section_name", "classroom_number")

    def dehydrate_school(self, obj):
        return obj.school_class.school.name if obj.school_class else ""

    def dehydrate_stream(self, obj):
        return obj.school_class.stream.name if obj.school_class and obj.school_class.stream else ""

    def dehydrate_medium(self, obj):
        return obj.school_class.medium.name if obj.school_class and obj.school_class.medium else ""

    def dehydrate_classroom_number(self, obj):
        return obj.classroom.room_number if obj.classroom else ""

class ClassroomAdmin(ImportExportModelAdmin):
    resource_class = ClassroomResource
    list_display = ("room_number", "school", "capacity", "floor")
    search_fields = ("room_number", "school__name")
    list_filter = ("school",)


class ClassAdmin(ImportExportModelAdmin):
    resource_class = ClassResource
    list_display = ("name", "school", "stream", "medium")
    search_fields = ("name", "school__name", "stream__name", "medium__name")
    list_filter = ("school", "stream", "medium")


class SectionAdmin(ImportExportModelAdmin):
    resource_class = SectionResource
    list_display = ("name", "school_class", "classroom")
    search_fields = ("name", "school_class__name", "school_class__school__name")
    list_filter = ("school_class__school",)



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



class ClassSubjectResource(resources.ModelResource):
    school = fields.Field(column_name="School", attribute="class_info", readonly=True)
    class_info = fields.Field(column_name="Class", attribute="class_info", widget=ClassInfoWidget(Class, "name"))
    stream = fields.Field(column_name="Stream", readonly=True)
    medium = fields.Field(column_name="Medium", readonly=True)
    subject = fields.Field(column_name="Subject", attribute="subject", widget=ForeignKeyWidget(Subject, "name"))
    periods_per_week = fields.Field(column_name="Periods Per Week", attribute="periods_per_week")
    is_optional = fields.Field(column_name="Is Optional", attribute="is_optional")
    has_lab = fields.Field(column_name="Has Lab", attribute="has_lab")

    class Meta:
        model = ClassSubject
        fields = (
            "id",
            "school",
            "class_info",
            "stream",
            "medium",
            "subject",
            "periods_per_week",
            "is_optional",
            "has_lab",
        )
        export_order = fields

    def dehydrate_school(self, obj):
        return obj.class_info.school.name if obj.class_info and obj.class_info.school else ""

    def dehydrate_stream(self, obj):
        return obj.class_info.stream.name if obj.class_info and obj.class_info.stream else ""

    def dehydrate_medium(self, obj):
        return obj.class_info.medium.name if obj.class_info and obj.class_info.medium else ""

class ClassSubjectAdmin(ImportExportModelAdmin):
    resource_class = ClassSubjectResource
    list_display = (
        "class_info",
        "get_stream",
        "get_medium",
        "subject",
        "periods_per_week",
        "is_optional",
        "has_lab",
    )

    @admin.display(description="Stream")
    def get_stream(self, obj):
        return obj.class_info.stream.name if obj.class_info and obj.class_info.stream else "—"

    @admin.display(description="Medium")
    def get_medium(self, obj):
        return obj.class_info.medium.name if obj.class_info and obj.class_info.medium else "—"

    search_fields = (
        "class_info__name",
        "class_info__school__name",
        "subject__name",
    )
    list_filter = ("class_info__school", "is_optional", "has_lab")



class ClassInchargeResource(resources.ModelResource):
    # Explicitly handle related fields
    section = fields.Field(
        column_name="Section",
        attribute="section",
        widget=ForeignKeyWidget(Section, "name")  # or use any unique identifier field
    )

    staff = fields.Field(
        column_name="Staff",
        attribute="staff",
        widget=ForeignKeyWidget(Staff, "name")  # assuming Staff has unique `name`
    )

    class Meta:
        model = ClassIncharge
        fields = (
            "id",
            "section",
            "staff",
            "assigned_date",
            "effective_from",
            "effective_to",
            "active",
        )
        export_order = fields

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

admin.site.register(Document,DocumentAdmin)
#admin.site.register(User)  


admin.site.register(Facility)
#admin.site.register(Nodal)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(ExtracurricularActivity)
admin.site.register(Committee)
admin.site.register(CommitteeMember)
admin.site.register(CommitteeMeeting)
admin.site.register(Department)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Section,SectionAdmin)
# admin.site.register(Subject)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Classroom,ClassroomAdmin)
admin.site.register(ClassIncharge,ClassInchargeAdmin)
admin.site.register(Timetable,TimetableAdmin)
# admin.site.register(TimetableSlot,TimetableSlotAdmin)
# admin.site.register(TimetableEntry,TimetableEntryAdmin)
admin.site.register(Student,StudentAdmin)

admin.site.register(Book)
admin.site.register(SMCMember,SMCMemberAdmin)
admin.site.register(TeacherSubjectAssignment,TeacherSubjectAssignmentAdmin)



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
