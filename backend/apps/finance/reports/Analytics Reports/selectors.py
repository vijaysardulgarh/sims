import django_filters

from apps.finance.student_fees.models import StudentFee


class StudentFeeFilter(django_filters.FilterSet):

    class Meta:
        model = StudentFee
        fields = [
            "session",
            "is_closed",
        ]