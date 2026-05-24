from django.urls import path

# from apps.students.views.student_views import (

#     StudentListCreateAPIView,

#     StudentRetrieveUpdateDestroyAPIView,
# )

from apps.students.profiles.import_export_api import (

    StudentImportAPIView,
)

from apps.students.profiles.import_export_api import (

    StudentExportAPIView,
)

urlpatterns = [

    # =====================================
    # STUDENT CRUD APIs
    # =====================================

    # path(
    #     "",
    #     StudentListCreateAPIView.as_view(),
    #     name="student_list_create"
    # ),

    # path(
    #     "<str:srn>/",
    #     StudentRetrieveUpdateDestroyAPIView.as_view(),
    #     name="student_detail"
    # ),

    # =====================================
    # IMPORT / EXPORT APIs
    # =====================================

    path(
        "import/",
        StudentImportAPIView.as_view(),
        name="student_import"
    ),

    path(
        "export/",
        StudentExportAPIView.as_view(),
        name="student_export"
    ),
]