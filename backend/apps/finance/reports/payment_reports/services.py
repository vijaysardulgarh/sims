from .selectors import (
    get_today_collection,
    payment_mode_summary,
)



def today_collection_service():

    data = get_today_collection()

    return {
        "today_collection": data["total"] or 0
    }



def payment_mode_service():

    return payment_mode_summary()