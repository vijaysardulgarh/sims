from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from ..models.school import School,Infrastructure,AboutSchool,Principal,Affiliation,MandatoryPublicDisclosure,Facility
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

class MandatoryPublicDisclosureResource(resources.ModelResource):
    class Meta:
        model = MandatoryPublicDisclosure
        fields = ("id", "section", "title", "value", "file", "order", "is_active")
        export_order = ("id", "section", "title", "value", "file", "order", "is_active")        


class FacilityResource(resources.ModelResource):
    class Meta:
        model = Facility
        fields = ("id", "school", "name", "description", "image")
        export_order = ("id", "school", "name", "description", "image")        