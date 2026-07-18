from django.urls import path

from .views import (

    GenerateTimetableView,
    CopyDayView,
    CopyWeekView,

)

urlpatterns = [

    path(
        "",
        GenerateTimetableView.as_view()
    ),

    path(
        "copy-day/",
        CopyDayView.as_view()
    ),

    path(
        "copy-week/",
        CopyWeekView.as_view()
    ),

]