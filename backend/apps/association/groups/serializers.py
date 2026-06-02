# =============================================================================
# groups/serializers/group_serializer.py
# =============================================================================

from rest_framework import serializers

from apps.documents.models import Document
from apps.associations.groups.models import (
    Group
)


class GroupSerializer(
    serializers.ModelSerializer
):

    # ============================================
    # DISPLAY FIELDS
    # ============================================

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    academic_session_name = serializers.CharField(
        source="academic_session.name",
        read_only=True
    )

    chairperson_name = serializers.CharField(
        source="chairperson.name",
        read_only=True
    )

    group_type_display = serializers.CharField(
        source="get_group_type_display",
        read_only=True
    )

    status_display = serializers.CharField(
        source="get_status_display",
        read_only=True
    )

    # ============================================
    # DOCUMENTS
    # ============================================

    document_ids = serializers.PrimaryKeyRelatedField(
        queryset=Document.objects.all(),
        many=True,
        write_only=True,
        source="documents",
        required=False
    )

    # ============================================
    # META
    # ============================================

    class Meta:

        model = Group   

        fields = [

            "id",

            "school",
            "school_name",

            "academic_session",
            "academic_session_name",

            "name",

            "group_type",
            "group_type_display",

            "status",
            "status_display",

            "chairperson",
            "chairperson_name",

            "tasks",
            "description",

            "documents",
            "document_ids",

            "show_on_website",

            "slug",
            "priority",

            "is_active",
            "is_deleted",

            "created_at",
            "updated_at",
        ]

        read_only_fields = [

            "slug",

            "created_at",
            "updated_at",

            "is_deleted",

            "documents",
        ]

    # ============================================
    # FIELD VALIDATION
    # ============================================

    def validate_name(self, value):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(
                "Group name cannot be empty"
            )

        return value

    # ============================================
    # OBJECT VALIDATION
    # ============================================

    def validate(self, attrs):

        school = attrs.get(
            "school",
            getattr(self.instance, "school", None)
        )

        chairperson = attrs.get(
            "chairperson",
            getattr(
                self.instance,
                "chairperson",
                None
            )
        )

        if (
            chairperson and
            chairperson.school != school
        ):

            raise serializers.ValidationError({

                "chairperson":
                    "Chairperson must belong "
                    "to same school"
            })

        return attrs