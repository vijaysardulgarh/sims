from apps.finance.student_fees.models import StudentFee



def get_pending_fees():

    return (
        StudentFee.objects
        .filter(due_amount__gt=0)
        .select_related(
            "student",
            "fee_structure"
        )
    )



def get_fully_paid_students():

    return (
        StudentFee.objects
        .filter(is_closed=True)
        .select_related("student")
    )