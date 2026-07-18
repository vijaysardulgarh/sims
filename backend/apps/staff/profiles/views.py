from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.staff.profiles.models import Staff
from apps.staff.profiles.serializers import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):

    # ============================================
    # SERIALIZER
    # ============================================

    serializer_class = StaffSerializer

    # ============================================
    # PERMISSIONS
    # ============================================

    permission_classes = [
        IsAuthenticated
    ]

    # ============================================
    # QUERYSET
    # ============================================

    queryset = (
        Staff.objects
        .select_related(
            "school",
            "post_type",
            "subject",
            "user",
        )
        .filter(
            is_deleted=False
        )
        .order_by("name")
    )

    # ============================================
    # FILTER BACKENDS
    # ============================================

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # ============================================
    # SEARCH
    # ============================================

    search_fields = [

        "employee_id",

        "name",

        "father_name",

        "mother_name",

        "spouse_name",

        "designation",

        "qualification",

        "email",

        "mobile_number",

        "aadhar_number",

        "school__name",

        "post_type__name",

        "subject__name",
    ]

    # ============================================
    # FILTERS
    # ============================================

    filterset_fields = [

        "school",

        "post_type",

        "subject",

        "designation",

        "staff_role",

        "employment_type",

        "status",

        "gender",

        "is_active",

        "is_class_teacher",

        "is_house_incharge",
    ]

    # ============================================
    # ORDERING
    # ============================================

    ordering_fields = [

        "employee_id",

        "name",

        "joining_date",

        "retirement_date",

        "priority",

        "designation",

        "status",

        "teaching_experience_years",
    ]

    ordering = [
        "name"
    ]

    # ============================================
    # SOFT DELETE
    # ============================================

    def perform_destroy(self, instance):

        instance.is_deleted = True

        instance.save(update_fields=["is_deleted"])