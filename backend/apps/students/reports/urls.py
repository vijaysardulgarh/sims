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

from .roll_call.views.views import (
    RollCallAPIView,
    RollCallFiltersAPIView,
)

from .roll_call.views.roll_call_excel import (
    RollCallExcelAPIView,
)

urlpatterns = [

    # ==========================
    # STUDENT STRENGTH
    # ==========================

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

    # ==========================
    # ROLL CALL
    # ==========================

    path(
        "roll-call/filters/",
        RollCallFiltersAPIView.as_view(),
        name="roll_call_filters",
    ),

    path(
        "roll-call/excel/",
        RollCallExcelAPIView.as_view(),
        name="roll_call_excel",
    ),

    path(
        "roll-call/",
        RollCallAPIView.as_view(),
        name="roll_call",
    ),

]