from django.urls import path

from .views import (
    SubjectRequirementListView,
    SubjectRequirementBulkSaveView,
)

urlpatterns = [
    path(
        "",
        SubjectRequirementListView.as_view(),
        name="subject-requirement-list",
    ),
    path(
        "bulk-save/",
        SubjectRequirementBulkSaveView.as_view(),
        name="subject-requirement-bulk-save",
    ),
]