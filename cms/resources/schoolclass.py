from import_export import resources, fields
from ..models.school import School
from ..models.schoolclass import Medium,Class,Section,Classroom,Stream
from import_export.widgets import ForeignKeyWidget

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

class SectionResource(resources.ModelResource):


    school = fields.Field(
        column_name='School',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name')
    )

    sec_class = fields.Field(
        column_name='Class',
        attribute='sec_class',
        widget=ForeignKeyWidget(Class, 'name')
    )

    name = fields.Field(column_name='Section', attribute='name')

    classroom = fields.Field(
        column_name='Room No',
        attribute='classroom',
        widget=ForeignKeyWidget(Classroom, 'name')
    )

    stream = fields.Field(
        column_name="Stream",
        attribute="stream",
        widget=ForeignKeyWidget(Stream, "name"),
        default=None
    )

    medium = fields.Field(
        column_name="Medium",
        attribute="medium",
        widget=ForeignKeyWidget(Medium, "name"),
        default=None
    )

    sub_stream = fields.Field(
        column_name="Sub Stream",
        attribute="sub_stream"
    )

    class Meta:
        model = Section
        import_id_fields = ('school', 'sec_class', 'name')
        fields = ('school', 'sec_class', 'name', 'classroom', 'stream', 'medium', 'sub_stream')
        export_order = ('id', 'school', 'sec_class', 'name', 'classroom', 'stream', 'medium', 'sub_stream')

    def before_import_row(self, row, **kwargs):
        school_name = row.get('School')
        class_name = row.get('Class')

        if not school_name or not class_name:
            raise Exception("Both 'School' and 'Class' columns are required in the import file.")

        # Validate School
        try:
            school = School.objects.get(name=school_name)
        except School.DoesNotExist:
            raise Exception(f"School '{school_name}' does not exist.")

        # Validate Class (must belong to the given School)
        try:
            sec_class = Class.objects.get(name=class_name, school=school)
        except Class.DoesNotExist:
            raise Exception(f"Class '{class_name}' does not exist for School '{school_name}'.")

        # Set IDs in row so FK widgets can resolve
        row['school'] = school.id
        row['sec_class'] = sec_class.id        

class StreamResource(resources.ModelResource):
    

    
    # ForeignKey to School
    school = fields.Field(
        column_name='School',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name')  # Maps school name to School instance
    )

    # Stream name
    name = fields.Field(column_name='Name', attribute='name')
    class Meta:
        model = Stream
        fields = ('school','name')
        export_order = ('school','name')
        import_id_fields = ('school','name')  # Use ID to update existing records




class ClassroomResource(resources.ModelResource):

    school = fields.Field(
        column_name='School',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name')
    )
    name = fields.Field(column_name='Room Number', attribute='name')
    capacity = fields.Field(column_name='Capacity', attribute='capacity')
    floor = fields.Field(column_name='Floor', attribute='floor')

    class Meta:
        model = Classroom
        fields = ('school', 'name', 'capacity', 'floor')
        export_order = ('school', 'name', 'capacity', 'floor')
        import_id_fields = ('school', 'name')  

class ClassResource(resources.ModelResource):
   
    school = fields.Field(
        column_name="School",
        attribute="school",
        widget=ForeignKeyWidget(School, "name")  # match by School.name
    )
    name = fields.Field(column_name="Class", attribute="name")
    
    class_order = fields.Field(column_name="Class Order", attribute="class_order")
    
    class Meta:
        model = Class
        fields = ("school", "name", "class_order")  # include stream, medium if needed
        export_order = ("school", "name", "class_order")
        import_id_fields = ("school", "name")  # ensures updates work using ID        