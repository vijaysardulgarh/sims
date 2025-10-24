from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
import datetime
import logging
from ..models.school import School
from ..models.staff import PostType,SanctionedPost,ClassIncharge
from ..models.subject import Subject
from ..models.staff import Staff,TeacherSubjectAssignment
from ..models.schoolclass import Section
from ..models.subject import ClassSubject

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
    max_periods_per_week= fields.Field(attribute='max_periods_per_week', column_name='Max Periods Per Week')
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
                "priority",
                "max_periods_per_week"
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
        

class TeacherSubjectAssignmentResource(resources.ModelResource):
    # Human-readable export fields with attribute mapping
    employee_id = fields.Field(
        column_name="Employee ID",
        attribute="teacher__employee_id"
    )
    teacher_name = fields.Field(
        column_name="Teacher",
        attribute="teacher__name"
    )
    designation = fields.Field(
        column_name="Designation",
        attribute="teacher__post_type__name"
    )
    school_name = fields.Field(
        column_name="School",
        attribute="section__sec_class__school__name"
    )
    class_name = fields.Field(
        column_name="Class",
        attribute="section__sec_class__name"
    )
    section_name = fields.Field(
        column_name="Section",
        attribute="section__name"
    )
    subject_name = fields.Field(
        column_name="Subject",
        attribute="class_subject__subject__name"
    )

    class Meta:
        model = TeacherSubjectAssignment
        fields = (
            "employee_id",
            "teacher_name",
            "designation",
            "school_name",
            "class_name",
            "section_name",
            "subject_name",
        )
        export_order = (
            "employee_id",
            "teacher_name",
            "designation",
            "school_name",
            "class_name",
            "section_name",
            "subject_name",
        )
        import_id_fields = ("employee_id", "class_name", "section_name", "subject_name")

    # ---------------- EXPORT HELPERS ----------------
    # (You can keep these if you want to override export formatting,
    # but with attribute mapping, preview will now work too.)
    def dehydrate_employee_id(self, obj):
        return obj.teacher.employee_id if obj.teacher else ""

    def dehydrate_teacher_name(self, obj):
        return obj.teacher.name if obj.teacher else ""

    def dehydrate_designation(self, obj):
        return obj.teacher.post_type.name if obj.teacher and obj.teacher.post_type else ""

    def dehydrate_school_name(self, obj):
        return obj.section.sec_class.school.name if obj.section else ""

    def dehydrate_class_name(self, obj):
        return obj.section.sec_class.name if obj.section else ""

    def dehydrate_section_name(self, obj):
        return obj.section.name if obj.section else ""

    def dehydrate_subject_name(self, obj):
        return obj.class_subject.subject.name if obj.class_subject else ""

    # ---------------- IMPORT HELPERS ----------------
    def before_import_row(self, row, row_number=None, **kwargs):
        errors = []
        emp_id = row.get("Employee ID", "").strip()
        designation = row.get("Designation", "").strip()
        class_name = row.get("Class", "").strip()
        section_name = row.get("Section", "").strip()
        subject_name = row.get("Subject", "").strip()

        # Validate teacher
        if emp_id and designation:
            if not Staff.objects.filter(
                employee_id=emp_id,
                post_type__name=designation,
                staff_role="Teaching"
            ).exists():
                errors.append(f"❌ Teacher '{emp_id} - {designation}' not found")

        # Validate section
        if class_name and section_name:
            if not Section.objects.filter(
                sec_class__name__iexact=class_name,
                name__iexact=section_name
            ).exists():
                errors.append(f"❌ Section '{class_name}-{section_name}' not found")

        # Validate subject
        if class_name and subject_name:
            if not ClassSubject.objects.filter(
                subject_class__name__iexact=class_name,
                subject__name__iexact=subject_name
            ).exists():
                errors.append(f"❌ Subject '{subject_name}' not found in class '{class_name}'")

        # Attach errors to preview
        row_result = kwargs.get("row_result")
        if errors and row_result:
            for error in errors:
                row_result.errors.append(error)

    def get_or_init_instance(self, instance_loader, row_data, **kwargs):
        emp_id = row_data.get("Employee ID", "").strip()
        designation = row_data.get("Designation", "").strip()
        class_name = row_data.get("Class", "").strip()
        section_name = row_data.get("Section", "").strip()
        subject_name = row_data.get("Subject", "").strip()

        teacher = Staff.objects.filter(
            employee_id=emp_id,
            post_type__name=designation,
            staff_role="Teaching"
        ).first()

        section = Section.objects.filter(
            sec_class__name__iexact=class_name,
            name__iexact=section_name
        ).first()

        class_subject = ClassSubject.objects.filter(
            subject_class__name__iexact=class_name,
            subject__name__iexact=subject_name
        ).first()

        # Check if assignment already exists
        instance = None
        if teacher and section and class_subject:
            instance = TeacherSubjectAssignment.objects.filter(
                teacher=teacher,
                section=section,
                class_subject=class_subject
            ).first()

        if instance:
            return instance, False
        else:
            return TeacherSubjectAssignment(
                teacher=teacher,
                section=section,
                class_subject=class_subject
            ), True
        
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

class PostTypeResource(resources.ModelResource):
    class Meta:
        model = PostType
        fields = ('id', 'name', 'description')  # specify fields for import/export
        export_order = ('id', 'name', 'description')        