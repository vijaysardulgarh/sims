from import_export import resources, fields
from ..models.school import School
from ..models.user import User

class UserResource(resources.ModelResource):
    school = fields.Field(
        column_name="School",
        attribute="school",
        widget=resources.widgets.ForeignKeyWidget(School, "name"),
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "school", "role", "is_active", "is_staff")
        export_order = ("id", "username", "email", "school", "role", "is_active", "is_staff")

    def before_save_instance(self, instance, using_transactions, dry_run):
        """
        Set default password as the username if password is missing.
        """
        if not instance.password or instance.password.strip() == "":
            instance.set_password(instance.username)  # 🔑 password = username  