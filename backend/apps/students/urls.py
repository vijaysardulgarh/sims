from django.urls import path
from django.urls import include

from apps.students.profiles.views import (

    StudentListCreateAPIView,

    StudentRetrieveUpdateDestroyAPIView,
)

from apps.students.profiles.import_export_api import (

    StudentImportAPIView,

    StudentExportAPIView,
)

urlpatterns = [

    path(
        "",
        StudentListCreateAPIView.as_view(),
        name="student_list_create",
    ),

    path(
        "import/",
        StudentImportAPIView.as_view(),
        name="student_import",
    ),

    path(
        "export/",
        StudentExportAPIView.as_view(),
        name="student_export",
    ),

    path(
        "reports/",
        include(
            "apps.students.reports.urls"
        )
    ),

    path(
        "<str:srn>/",
        StudentRetrieveUpdateDestroyAPIView.as_view(),
        name="student_detail",
    ),

]