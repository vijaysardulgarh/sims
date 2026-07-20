from django.urls import path

from .views import (
    TeacherPreferenceListView,
    TeacherPreferenceBulkSaveView,
)

urlpatterns = [
    path(
        "",
        TeacherPreferenceListView.as_view(),
        name="teacher-preference-list",
    ),
    path(
        "save/",
        TeacherPreferenceBulkSaveView.as_view(),
        name="teacher-preference-bulk-save",
    ),
]