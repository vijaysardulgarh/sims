# =============================================================================
# schools/urls.py
# =============================================================================

from django.urls import path

from apps.schools.views import (

    SchoolListAPIView,

    SelectSchoolAPIView,

    ClearSchoolAPIView,

    CurrentSchoolAPIView,
)

urlpatterns = [

    # =====================================
    # SCHOOL LIST
    # =====================================

    path(

        "",

        SchoolListAPIView.as_view(),

        name="school-list"
    ),

    # =====================================
    # SELECT SCHOOL
    # =====================================

    path(

        "select/",

        SelectSchoolAPIView.as_view(),

        name="select-school"
    ),

    # =====================================
    # CLEAR SCHOOL
    # =====================================

    path(

        "clear/",

        ClearSchoolAPIView.as_view(),

        name="clear-school"
    ),

    # =====================================
    # CURRENT SCHOOL
    # =====================================

    path(

        "current/",

        CurrentSchoolAPIView.as_view(),

        name="current-school"
    ),
]