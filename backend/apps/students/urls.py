from django.urls import path

from apps.students.profiles.views import (

    StudentListCreateAPIView,

    StudentRetrieveUpdateDestroyAPIView,
)

from apps.students.profiles.import_export_api import (

    StudentImportAPIView,

    StudentExportAPIView,
)


urlpatterns = [

    # =====================================
    # STUDENT LIST CREATE
    # =====================================

    path(

        "",

        StudentListCreateAPIView.as_view(),

        name="student_list_create",
    ),

    # =====================================
    # IMPORT / EXPORT APIs
    # =====================================

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

    # =====================================
    # STUDENT DETAIL APIs
    # =====================================

    path(

        "<str:srn>/",

        StudentRetrieveUpdateDestroyAPIView.as_view(),

        name="student_detail",
    ),
]