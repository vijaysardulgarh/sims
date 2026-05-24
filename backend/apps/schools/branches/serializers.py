from rest_framework import serializers

from apps.schools.branches.models import (
    Branch
)


# ==========================================
# BRANCH SERIALIZER
# ==========================================

class BranchSerializer(
    serializers.ModelSerializer
):

    # ======================================
    # EXTRA READ FIELDS
    # ======================================

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    created_by_email = serializers.CharField(
        source="created_by.email",
        read_only=True
    )

    updated_by_email = serializers.CharField(
        source="updated_by.email",
        read_only=True
    )

    # ======================================
    # META
    # ======================================

    class Meta:

        model = Branch

        fields = [

            "id",

            "school",

            "school_name",

            "name",

            "code",

            "address",

            "phone",

            "is_active",

            "is_deleted",

            "created_at",

            "updated_at",

            "created_by",

            "created_by_email",

            "updated_by",

            "updated_by_email",
        ]

        read_only_fields = [

            "id",

            "school",

            "created_at",

            "updated_at",

            "created_by",

            "updated_by",

            "created_by_email",

            "updated_by_email",
        ]

    # ======================================
    # VALIDATE CODE
    # ======================================

    def validate_code(
        self,
        value
    ):

        return value.upper().strip()

    # ======================================
    # VALIDATE
    # ======================================

    def validate(
        self,
        attrs
    ):

        request = self.context.get(
            "request"
        )

        school = getattr(
            request,
            "school",
            None
        )

        code = attrs.get(
            "code"
        )

        queryset = Branch.objects.filter(

            school=school,

            code=code,

            is_deleted=False
        )

        if self.instance:

            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():

            raise serializers.ValidationError(

                {
                    "code":
                    "Branch code already exists."
                }
            )

        return attrs