from .selectors import (
    get_total_fee_amount,
    get_total_collected_amount,
    get_total_due_amount,
    get_pending_students_count,
)



def finance_dashboard_service():

    total_fee = get_total_fee_amount()
    total_collected = get_total_collected_amount()
    total_due = get_total_due_amount()
    pending_students = get_pending_students_count()

    return {
        "total_fee": total_fee["total"] or 0,
        "total_collected": total_collected["total"] or 0,
        "total_due": total_due["total"] or 0,
        "pending_students": pending_students,
    }