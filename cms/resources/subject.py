from import_export import resources, fields
from ..models.subject import Subject,ClassSubject
from ..models.schoolclass import Class,Stream
from import_export.widgets import ForeignKeyWidget,BooleanWidget
class SubjectResource(resources.ModelResource):

    name = fields.Field(column_name='Name of Subject', attribute='name')
    class Meta:
        model = Subject
        import_id_fields = ('name',)
        fields = ("name",)
        export_order = ("name",)


class ClassSubjectResource(resources.ModelResource):
    # Export-only field
    school = fields.Field(column_name="School")

    subject_class = fields.Field(
        column_name="Class",
        attribute="subject_class",
        widget=ForeignKeyWidget(Class, "name"),
    )
    stream = fields.Field(
        column_name="Stream",
        attribute="stream",
        widget=ForeignKeyWidget(Stream, "name"),
    )
    subject = fields.Field(
        column_name="Subject",
        attribute="subject",
        widget=ForeignKeyWidget(Subject, "name"),
    )
    theory_periods_per_week = fields.Field(
        column_name="Theory Periods Per Week",
        attribute="theory_periods_per_week",
    )
    practical_periods_per_week = fields.Field(
        column_name="Practical Periods Per Week",
        attribute="practical_periods_per_week",
    )
    periods_per_week = fields.Field(
        column_name="Periods Per Week",
        attribute="periods_per_week",
    )
    

    is_optional = fields.Field(column_name="Is Optional", attribute="is_optional", widget=BooleanWidget())
    has_lab = fields.Field(column_name="Has Lab", attribute="has_lab", widget=BooleanWidget())
    is_shared = fields.Field(column_name="Is Shared", attribute="is_shared", widget=BooleanWidget())

    class Meta:
        model = ClassSubject
        import_id_fields = ("subject_class", "stream", "subject")
        fields = (
            "school", "subject_class", "stream", "subject",
            "theory_periods_per_week", "practical_periods_per_week",
            "periods_per_week", "is_optional", "has_lab", "is_shared",
        )
        skip_unchanged = True
        report_skipped = True

    # Ensure Booleans are never None
    def before_import_row(self, row, **kwargs):
        if not row.get("Is Optional"):
            row["Is Optional"] = False
        if not row.get("Has Lab"):
            row["Has Lab"] = False
        if not row.get("Is Shared"):
            row["Is Shared"] = False

        # Optional stream: allow blank
        if not row.get("Stream"):
            row["Stream"] = None

    def dehydrate_school(self, obj):
        return obj.subject_class.school.name if obj.subject_class and obj.subject_class.school else ""

    def dehydrate_subject_class(self, obj):
        return obj.subject_class.name if obj.subject_class else ""

    def dehydrate_stream(self, obj):
        return obj.stream.name if obj.stream else ""

    def dehydrate_subject(self, obj):
        return obj.subject.name if obj.subject else ""        