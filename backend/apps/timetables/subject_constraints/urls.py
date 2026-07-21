from django.urls import path

from .views import (
    SubjectConstraintListView,
    SubjectConstraintBulkSaveView,
)

urlpatterns = [

    path(
        "",
        SubjectConstraintListView.as_view(),
        name="subject-constraint-list",
    ),

    path(
        "bulk-save/",
        SubjectConstraintBulkSaveView.as_view(),
        name="subject-constraint-bulk-save",
    ),

]