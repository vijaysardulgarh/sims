from django.db.models import Sum

from apps.finance.student_fees.models import StudentFee
from apps.finance.fee_payments.models import FeePayment


def get_total_fee_amount():
    return (
        StudentFee.objects
        .aggregate(total=Sum("total_amount"))
    )



def get_total_collected_amount():
    return (
        FeePayment.objects
        .aggregate(total=Sum("amount"))
    )



def get_total_due_amount():
    return (
        StudentFee.objects
        .aggregate(total=Sum("due_amount"))
    )



def get_pending_students_count():
    return (
        StudentFee.objects
        .filter(due_amount__gt=0)
        .count()
    )