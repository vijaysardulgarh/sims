from rest_framework import serializers

from apps.staff.class_incharge.models import ClassIncharge


class ClassInchargeSerializer(serializers.ModelSerializer):

    staff_name = serializers.CharField(
        source="staff.name",
        read_only=True,
    )

    employee_id = serializers.CharField(
        source="staff.employee_id",
        read_only=True,
    )

    section_name = serializers.CharField(
        source="section.name",
        read_only=True,
    )

    class_name = serializers.CharField(
        source="section.class_obj.name",
        read_only=True,
    )

    class Meta:

        model = ClassIncharge

        fields = [
            "id",

            # Section
            "section",
            "section_name",
            "class_name",

            # Staff
            "staff",
            "staff_name",
            "employee_id",

            # Assignment
            "assigned_date",
            "effective_from",
            "effective_to",
            "active",
            "remarks",

            # Audit (from SchoolBaseModel)
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "assigned_date",
            "staff_name",
            "employee_id",
            "section_name",
            "class_name",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):

        effective_from = attrs.get(
            "effective_from",
            getattr(self.instance, "effective_from", None),
        )

        effective_to = attrs.get(
            "effective_to",
            getattr(self.instance, "effective_to", None),
        )

        if (
            effective_from
            and effective_to
            and effective_to < effective_from
        ):
            raise serializers.ValidationError(
                {
                    "effective_to":
                    "Effective To must be after Effective From."
                }
            )

        return attrs