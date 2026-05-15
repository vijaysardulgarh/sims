from .selectors import (
    get_pending_fees,
    get_fully_paid_students,
)



def pending_fee_report_service():

    queryset = get_pending_fees()

    return {
        "count": queryset.count(),
        "results": queryset,
    }



def fully_paid_report_service():

    queryset = get_fully_paid_students()

    return {
        "count": queryset.count(),
        "results": queryset,
    }