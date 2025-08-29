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
from .models import Day
from .models import TimetableSlot
from .models import TeacherSubjectAssignment
from .models import TimetableEntry
from .models import Student,FeeStructure
from .models import PostType,FAQ
from .models import Book,Infrastructure,SanctionedPost
from .models import SMCMember,AboutSchool,Principal,Association,AssociationType,AssociationRole,StaffAssociationRoleAssignment
import logging
from .models import StudentAchievement, ExamDetail
 
admin.site.site_header="SIMS" 
admin.site.site_title="SIMS"
admin.site.index_title="School Information Management System"
class StaffResource(resources.ModelResource):
    employee_id = fields.Field(attribute='employee_id',column_name='Employee ID')
    school = fields.Field(attribute='school',column_name='School',widget=ForeignKeyWidget(School, field='name'))
    name = fields.Field(attribute='name',column_name='Employee Name [ID]')
    father_name = fields.Field(attribute='father_name',column_name="Father's Name")
    mother_name = fields.Field(attribute='mother_name',column_name="Mother's Name")
    spouse_name = fields.Field(attribute='spouse_name',column_name='Spouse Name')
    gender = fields.Field(attribute='gender',column_name='Gender')
    aadhar_number = fields.Field(attribute='aadhar_number',column_name='Aadhar No')
    post_type = fields.Field(attribute='post_type',column_name='Post Type',widget=ForeignKeyWidget(PostType, field='name'))
    category = fields.Field(attribute='category',column_name='Category')
    date_of_birth = fields.Field(attribute='date_of_birth',column_name='Date of Birth')
    joining_date = fields.Field(attribute='joining_date',column_name='Date of Joining School/Office')
    current_joining_date = fields.Field(attribute='current_joining_date',column_name='Date of Joining School/Office')
    retirement_date = fields.Field(attribute='retirement_date',column_name='Retirement Date')
    qualification= fields.Field(attribute='qualification',column_name='Qualification')
    subject = fields.Field(attribute='subject',column_name='Subject',widget=ForeignKeyWidget(Subject, field='name'))
    email = fields.Field(attribute='email',column_name='Email ID')
    mobile_number = fields.Field(attribute='mobile_number',column_name='Mobile Number')
    # teaching_subject_1 = fields.Field(attribute='teaching_subject_1',column_name='Teaching Subject 1',widget=ForeignKeyWidget(Subject, field='name'))
    # teaching_subject_2 = fields.Field(attribute='teaching_subject_1',column_name='Teaching Subject 2',widget=ForeignKeyWidget(Subject, field='name'))
    staff_role = fields.Field(attribute='staff_role',column_name='Staff Role')
    employment_type = fields.Field(attribute='employment_type',column_name='Employment Type')
    #designation = fields.Field(attribute='designation',column_name='Designation')
    priority = fields.Field(attribute='priority', column_name='Priority') 
    class Meta:
        model = Staff
        fields=('id',"employee_id","name","father_name","mother_name","spouse_name","gender","aadhar_number","category","date_of_birth","joining_date","retirement_date","qualification","email","mobile_number","subject","staff_role","employment_type","post_type")

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
        "employee_id", "name", "father_name", "mother_name", "spouse_name",
        "gender", "aadhar_number", "post_type", "category", "date_of_birth",
        "joining_date", "current_joining_date", "retirement_date",
        "qualification", "subject", "email", "mobile_number","school",
        "staff_role", "employment_type", "priority"  # ✅ added priority in admin
    )
    list_filter = ("school", "staff_role", "employment_type", "gender", "category")
    search_fields = ("name", "employee_id", "email", "mobile_number")
    ordering = ("priority", "name")  # ✅ staff ordered by priority then name
    resource_class = StaffResource

class StudentResource(resources.ModelResource):
    
    srn = fields.Field(attribute='srn',column_name='SRN')
    stream = fields.Field(attribute='stream',column_name='Stream')
    studentclass = fields.Field(attribute='studentclass',column_name='Class')
    section = fields.Field(attribute='section',column_name='Section')
    roll_number = fields.Field(attribute='roll_number',column_name='Roll Number')
    full_name_aadhar = fields.Field(attribute='full_name_aadhar',column_name='FullName as on Aadhar Card')
    father_full_name_aadhar = fields.Field(attribute='father_full_name_aadhar',column_name="Father's Full Name aso on Aadhar Card")
    mother_full_name_aadhar = fields.Field(attribute='mother_full_name_aadhar',column_name="Mother's Full Name as on Aadhaar")
    
    date_of_birth = fields.Field(attribute='date_of_birth',column_name='Date of Birth')
    gender = fields.Field(attribute='gender',column_name='Gender')
    aadhaar_number = fields.Field(attribute='aadhaar_number',column_name='Aadhaar Number (If any)')
    category = fields.Field(attribute='category', column_name='Category Name')
    admission_number = fields.Field(attribute='admission_number',column_name='Admission Number')
    admission_date = fields.Field(attribute='admission_date',column_name='Admission Date')
    father_mobile = fields.Field(attribute='father_mobile',column_name="Father's Mobile No")
    mother_mobile = fields.Field(attribute='mother_mobile', column_name="Mother's Mobile No")
    bank_name = fields.Field(attribute='bank_name', column_name='Bank Name')
    ifsc = fields.Field(attribute='ifsc', column_name='IFSC')
    account_number = fields.Field(attribute='account_number', column_name='Account Number')
    disability = fields.Field(attribute='disability', column_name='Disability')
    disorder = fields.Field(attribute='disorder', column_name='Disorder Name')
    subjects_opted = fields.Field(attribute='subjects_opted', column_name='Subjects opted by student')
    stream = fields.Field(attribute='stream',column_name='Stream')
    school_code = fields.Field(attribute='school_code',column_name='SchoolCode')
    school_name = fields.Field(attribute='school_name',column_name='SchoolName')
    domicile_of_haryana = fields.Field(attribute='domicile_of_haryana',column_name='Domicile Of Haryana?')
    father_aadhaar_number = fields.Field(attribute='father_aadhaar_number',column_name="Father's Aadhaar Number")
    mother_aadhaar_number = fields.Field(attribute='mother_aadhaar_number',column_name="Mother's Aadhaar Number")
    guardian_full_name_aadhar = fields.Field(attribute='guardian_full_name_aadhar',column_name="Guardian's Full Name as on Aadhar Card")
    guardian_aadhaar_number = fields.Field(attribute='guardian_aadhaar_number',column_name="Guardian's Aadhar Nummber")
    family_annual_income = fields.Field(attribute='family_annual_income',column_name='Family Annual Income')
    state = fields.Field(attribute='state',column_name='State')
    district = fields.Field(attribute='district',column_name='District')
    block = fields.Field(attribute='block',column_name='CD Block')
    sub_district = fields.Field(attribute='sub_district',column_name='Sub-district/Tehsil')
    city_village_town = fields.Field(attribute='city_village_town',column_name='City/Village/Town')
    address = fields.Field(attribute='address',column_name='Adress Line 1')
    postal_code = fields.Field(attribute='postal_code',column_name='Postalcode')
    guardian_mobile = fields.Field(attribute='mother_mobile', column_name="Guardian's Mobile No")
    caste = fields.Field(attribute='caste_name', column_name='Caste Name')
    bpl_certificate_issuing_authority=fields.Field(attribute='bpl_certificate_issuing_authority',column_name='BPL Certificate Issuing Authority')
    
    class Meta:
        model = Student
        #exclude = ('id',)
        fields = ('srn', 'stream','school_code', 'school_name', 'admission_date', 'class', 'stream', 'section', 'roll_number', 'admission_number','admission_date','title', 'excel_full_name_aadhar', 'name_in_local_language', 'date_of_birth', 'gender', 'aadhaar_number', 'eid_number', 'domicile_of_haryana', 'nationality', 'excel_birth_country', 'birth_state', 'birth_district', 'birth_sub_district', 'birth_city_village_town','subjects_opted','subjects') 
        import_id_fields = ['srn']
        export_order = ('srn','stream','studentclass','section','roll_number','full_name_aadhar','father_full_name_aadhar','mother_full_name_aadhar','date_of_birth','gender','aadhaar_number','category','admission_number','father_mobile','subjects')
        #widgets = {
        #    'admission_date': {'format': '%d/%m/%Y'},  # Format for date fields
        #    'date_of_birth': {'format': '%d/%m/%Y'},  # Format for date fields
        #    'bpl_certificate_issued_date': {'format': '%d/%m/%Y'},  # Format for date fields
        #    'sibling_date_of_birth': {'format': '%d/%m/%Y'},  # Format for date fields
        #    # Widgets for boolean fields
       
        #}       
        def before_import(self, dataset, using_transactions, dry_run, **kwargs):
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
        
class StudentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    
    resource_class=StudentResource
    list_display=('srn','stream','studentclass','section','roll_number','full_name_aadhar','father_full_name_aadhar','mother_full_name_aadhar','date_of_birth','gender','aadhaar_number','category','admission_number','father_mobile','subjects_opted','subjects')

    
    
class TimetableSlotResource(resources.ModelResource):

    period = fields.Field(attribute='period',column_name='Period Count')
    start_time = fields.Field(attribute='start_time',column_name='Start Time')
    end_time = fields.Field(attribute='end_time',column_name='End Time')

    class Meta:
        model = TimetableSlot
        fields=('period','start_time','end_time')
        #use_id=False

class TimetableSlotAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('period','start_time','end_time')
    resource_class=TimetableSlotResource



class TeacherSubjectAssignmentResource(resources.ModelResource):
    
    teacher = fields.Field(attribute='teacher',column_name='Teacher')
    subject = fields.Field(attribute='subject',column_name='Subject')
    class_name = fields.Field(attribute='class_name',column_name='Class Name')
    maximum_periods_per_teacher = fields.Field(attribute='periods',column_name='Maximum Periods Per Teacher')
    periods_per_week = fields.Field(attribute='periods_per_week',column_name='Maximum Periods Per Subject Per Week')
    class Meta:
        model = TeacherSubjectAssignment
        fields=('id','class_name','subject','teacher','maximum_periods_per_teacher','periods_per_week')
        #use_id=False    

    

class TeacherSubjectAssignmentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('class_name','subject','teacher','maximum_periods_per_teacher','periods_per_week')
    resource_class=TeacherSubjectAssignmentResource
    
    def get_queryset(self, request):
        # Return only teaching staff
        return TeacherSubjectAssignment.objects.filter(teacher__staff_role='Teaching')

class TimetableEntryResource(resources.ModelResource):
    section = fields.Field(attribute='section',column_name='Section')
    subject = fields.Field(attribute='subject',column_name='Subject')
    teacher = fields.Field(attribute='teacher',column_name='Teacher')
    slot = fields.Field(attribute='slot',column_name='Slot')

    class Meta:
        model = TimetableEntry
        fields=('section','subject','teacher','slot')
        #use_id=False

class TimetableEntryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('section','subject','teacher','slot')
    resource_class=TimetableEntryResource    


class TimetableResource(resources.ModelResource):
    class_name = fields.Field(attribute='class_name',column_name='Class')
    section = fields.Field(attribute='section',column_name='Section')
    subject = fields.Field(attribute='subject',column_name='Subject')
    day = fields.Field(attribute='day',column_name='Subject')
    period=fields.Field(attribute="period",column_name="Period")
    start_time = fields.Field(attribute='start_time',column_name='Subject')
    end_time = fields.Field(attribute='end_time',column_name='Subject')
    class_name = fields.Field(attribute='class_name',column_name='Class')
    section = fields.Field(attribute='section',column_name='Section')
    #classrooms = fields.Field(attribute='classrooms',column_name='Subject')
    teachers = fields.Field(attribute='teachers',column_name='Teachers' )
    #slot = fields.Field(attribute='slot',column_name='Slot')

    class Meta:
        model = Timetable
        fields=('day','period','start_time','end_time','class_name','section','subject','teachers')
        #use_id=False

class TimetableAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('day','period','start_time','end_time','class_name','section','subject','teacher_name')

    def teacher_name(self, obj):
        return obj.teachers.name
    
    resource_class=TimetableResource   

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
admin.site.register(Stream)
admin.site.register(Class)
admin.site.register(Section)
# admin.site.register(Subject)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Classroom)
admin.site.register(ClassIncharge)
admin.site.register(Timetable,TimetableAdmin)
admin.site.register(TimetableSlot,TimetableSlotAdmin)
admin.site.register(TimetableEntry,TimetableEntryAdmin)
admin.site.register(Student,StudentAdmin)

admin.site.register(Book)
admin.site.register(SMCMember,SMCMemberAdmin)
admin.site.register(TeacherSubjectAssignment,TeacherSubjectAssignmentAdmin)





