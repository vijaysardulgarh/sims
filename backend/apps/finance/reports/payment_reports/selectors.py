from django.db.models import Sum
from django.utils import timezone

from apps.finance.fee_payments.models import FeePayment



def get_today_collection():

    today = timezone.now().date()

    return (
        FeePayment.objects
        .filter(payment_date=today)
        .aggregate(total=Sum("amount"))
    )



def payment_mode_summary():

    return (
        FeePayment.objects
        .values("payment_mode")
        .annotate(total=Sum("amount"))
    )