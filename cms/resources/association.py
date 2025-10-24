from import_export import resources, fields
from ..models.association import SMCMember,AssociationType,Association,AssociationRole,StaffAssociationRoleAssignment
from ..models.staff import Staff
from ..models.school import School
from import_export.widgets import ForeignKeyWidget

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
