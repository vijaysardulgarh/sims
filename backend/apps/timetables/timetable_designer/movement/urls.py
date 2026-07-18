from django.urls import path

from .views import (
    MoveEntryView,
)

urlpatterns = [

    path(
        "",
        MoveEntryView.as_view()
    ),

]