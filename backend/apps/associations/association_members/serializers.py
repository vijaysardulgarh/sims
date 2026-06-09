# =============================================================================
# associations/serializers/association_member_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.associations.association_members.models import (
    AssociationMember
)


class AssociationMemberSerializer(
    serializers.ModelSerializer
):

    association_name = serializers.CharField(
        source="association.name",
        read_only=True
    )

    staff_name = serializers.CharField(
        source="staff.name",
        read_only=True
    )

    student_name = serializers.CharField(
        source="student.full_name",
        read_only=True
    )

    member_name = serializers.SerializerMethodField()

    class Meta:

        model = AssociationMember

        fields = [

            "id",

            "academic_session",

            "association",
            "association_name",

            "member_type",

            "staff",
            "staff_name",

            "student",
            "student_name",

            "external_name",
            "external_email",
            "external_phone_number",
            "external_designation",

            "member_name",

            "image",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

        read_only_fields = (

            "created_at",

            "updated_at",

            "association_name",

            "staff_name",

            "student_name",

            "member_name",
        )

    def get_member_name(
        self,
        obj
    ):

        if obj.staff:
            return obj.staff.name

        if obj.student:
            return getattr(
                obj.student,
                "full_name",
                str(obj.student)
            )

        return obj.external_name

    def validate(
        self,
        attrs
    ):

        member_type = attrs.get(
            "member_type",
            getattr(
                self.instance,
                "member_type",
                None
            )
        )

        staff = attrs.get(
            "staff",
            getattr(
                self.instance,
                "staff",
                None
            )
        )

        student = attrs.get(
            "student",
            getattr(
                self.instance,
                "student",
                None
            )
        )

        external_name = attrs.get(
            "external_name",
            getattr(
                self.instance,
                "external_name",
                ""
            )
        )

        if member_type == "STAFF":

            if not staff:

                raise serializers.ValidationError(
                    {
                        "staff":
                        "Staff is required."
                    }
                )

            if student:

                raise serializers.ValidationError(
                    {
                        "student":
                        "Student must be empty."
                    }
                )

        elif member_type == "STUDENT":

            if not student:

                raise serializers.ValidationError(
                    {
                        "student":
                        "Student is required."
                    }
                )

            if staff:

                raise serializers.ValidationError(
                    {
                        "staff":
                        "Staff must be empty."
                    }
                )

        elif member_type == "EXTERNAL":

            if not external_name:

                raise serializers.ValidationError(
                    {
                        "external_name":
                        "External member name is required."
                    }
                )

            if staff or student:

                raise serializers.ValidationError(
                    (
                        "External member "
                        "cannot have "
                        "staff or student."
                    )
                )

        return attrs