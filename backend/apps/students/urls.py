from django.urls import path
from .report_views import *
from .report_signin import SigninLinkAPIView, SigninPDFAPIView
from .report_rollcall import RollCallLinkAPIView, RollCallPDFAPIView
from .report_subject import SubjectReportLinkAPIView, SubjectReportPDFAPIView
from .report_bank import BankReportLinkAPIView, BankReportPDFAPIView
from .report_cwsn import CWSNStudentsReportAPIView
from .report_bpl import BPLStudentsReportAPIView
from .report_subject_strength import SubjectStrengthReportAPIView
from .report_student_strength import StudentStrengthReportAPIView
from .report_cbse_enrollment import (
    CBSEEnrollmentPDFAPIView,
    CBSEEnrollmentCSVAPIView
)
from .report_subject_wise import (
    SubjectWiseLinkAPIView,
    SubjectWiseStudentsPDFAPIView
)

urlpatterns = [

    # LINK APIs

path("signin-link/", SigninLinkAPIView.as_view()),
path("rollcall-link/", RollCallLinkAPIView.as_view()),
path("subject-link/", SubjectReportLinkAPIView.as_view()),
path("bank-link/", BankReportLinkAPIView.as_view()),

    # PDF APIs
path("signin/<str:class_name>/<str:section_name>/", SigninPDFAPIView.as_view()),
path("rollcall/<str:class_name>/<str:section_name>/", RollCallPDFAPIView.as_view()),  
path("subject/<str:class_name>/<str:section_name>/", SubjectReportPDFAPIView.as_view()),  
path("bank/<str:class_name>/<str:section_name>/", BankReportPDFAPIView.as_view()),

path("cwsn/", CWSNStudentsReportAPIView.as_view()),
path("bpl/", BPLStudentsReportAPIView.as_view()),
path("subject-strength/", SubjectStrengthReportAPIView.as_view()),
path("student-strength/", StudentStrengthReportAPIView.as_view()),
path("cbse/pdf/", CBSEEnrollmentPDFAPIView.as_view()),
path("cbse/csv/", CBSEEnrollmentCSVAPIView.as_view()),
path("subject-wise/options/", SubjectWiseLinkAPIView.as_view()),
path("subject-wise/<str:class_name>/<str:subject_name>/", SubjectWiseStudentsPDFAPIView.as_view()),


]