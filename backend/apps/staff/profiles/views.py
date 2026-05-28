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

        "email",

        "mobile_number",

        "aadhar_number",

        "school__name",
    ]

    # ============================================
    # FILTERS
    # ============================================

    filterset_fields = [

        "school",

        "post_type",

        "staff_role",

        "employment_type",

        "gender",

        "subject",

        "is_active",
    ]

    # ============================================
    # ORDERING
    # ============================================

    ordering_fields = [

        "employee_id",

        "name",

        "joining_date",

        "priority",
    ]

    ordering = [
        "name"
    ]

    # ============================================
    # SOFT DELETE
    # ============================================

    def perform_destroy(self, instance):

        instance.is_deleted = True

        instance.save()