from django.urls import path

from .student_strength.views.student_strength import (
    StudentStrengthAPIView
)

from .student_strength.views.student_strength_excel import (
    StudentStrengthExcelAPIView
)

from .student_strength.views.student_strength_pdf import (
    StudentStrengthPDFAPIView
)

urlpatterns = [

    path(
        "student-strength/",
        StudentStrengthAPIView.as_view(),
        name="student_strength",
    ),

    path(
        "student-strength/excel/",
        StudentStrengthExcelAPIView.as_view(),
        name="student_strength_excel",
    ),

    path(
        "student-strength/pdf/",
        StudentStrengthPDFAPIView.as_view(),
        name="student_strength_pdf",
    ),

]