from django.urls import path, include

from rest_framework.routers import (
    DefaultRouter
)

from apps.students.api.student_api import (
    StudentViewSet
)

from apps.students.api.import_export_api import (

    StudentImportAPIView,

    StudentExportAPIView,
)

router = DefaultRouter()

router.register(
    r"students",
    StudentViewSet
)

urlpatterns = [

    path(
        "",
        include(router.urls)
    ),

    path(
        "students/import/",
        StudentImportAPIView.as_view(),
    ),

    path(
        "students/export/",
        StudentExportAPIView.as_view(),
    ),
]