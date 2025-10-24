from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from ..models.school import School
from ..models.timetable import Day
from ..models.timetable import TimetableSlot,Timetable
from ..models.staff import Staff
from ..models.schoolclass import Section,Classroom,Class
from ..models.subject import Subject,ClassSubject

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
            return ClassSubject.objects.get(subject_class=class_obj, subject=subject_obj)
        except (Class.DoesNotExist, Subject.DoesNotExist, ClassSubject.DoesNotExist):
            raise ValueError(f"ClassSubject not found for Class '{class_name}' and Subject '{subject_name}'")
        
class SchoolWidget(ForeignKeyWidget):
    def __init__(self):
        super().__init__(School, "name")

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
                
class DayResource(resources.ModelResource):
    # Use ForeignKeyWidget for the related school
    school = fields.Field(
        column_name='School',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name')  # map School by its 'name' field
    )
    name = fields.Field(column_name='Day', attribute='name')
    sequence = fields.Field(column_name='Sequence', attribute='sequence')

    class Meta:
        model = Day
        fields = ("school", "name", "sequence")
        export_order = ("school", "name", "sequence")
        import_id_fields = ("school", "name")

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

    sequence_number = fields.Field(column_name="Sequence No.", attribute="sequence_number")
    period_number = fields.Field(column_name="Period No.", attribute="period_number")
    start_time = fields.Field(column_name="Start Time", attribute="start_time")
    end_time = fields.Field(column_name="End Time", attribute="end_time")
    is_break = fields.Field(column_name="Is Break", attribute="is_break")
    is_assembly = fields.Field(column_name="Is Assembly", attribute="is_assembly")
    is_special_event = fields.Field(column_name="Is Special Event", attribute="is_special_event")

    class Meta:
        model = TimetableSlot
        fields = (
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
