from django.db.models import Sum
from django.db.models.functions import TruncMonth

from apps.finance.fee_payments.models import FeePayment



def monthly_collection_chart():

    return (
        FeePayment.objects
        .annotate(month=TruncMonth("payment_date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )