from django.urls import path

from .views import (
    ConflictCheckView,
)

urlpatterns = [

    path(
        "",
        ConflictCheckView.as_view()
    ),

]