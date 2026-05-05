from django.urls import path
from .views import *

urlpatterns = [
    path("", SchoolListAPIView.as_view()),             # GET all schools
    path("select/", SelectSchoolAPIView.as_view()),    # POST select school
    path("clear/", ClearSchoolAPIView.as_view()),      # POST clear session
    path("current/", CurrentSchoolAPIView.as_view()),  # GET current school
]