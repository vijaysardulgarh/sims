from django.urls import path

from .views import (
    WorkingDayListView,
    WorkingDayBulkUpdateView,
)

urlpatterns = [
    path(
        "",
        WorkingDayListView.as_view(),
        name="working-day-list",
    ),

    path(
        "save/",
        WorkingDayBulkUpdateView.as_view(),
        name="working-day-save",
    ),
]