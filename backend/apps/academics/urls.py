from django.urls import path
from .timetable_api import *

urlpatterns += [

    path("timetable/generate/", TimetableGenerateAPIView.as_view()),
    path("timetable/assign/", TeacherAssignmentAPIView.as_view()),
    path("timetable/subjects/", SubjectsBySectionAPIView.as_view()),

    path("timetable/create/", TimetableCreateAPIView.as_view()),
    path("timetable/list/", TimetableListAPIView.as_view()),

    path("timetable/dashboard/", TimetableDashboardAPIView.as_view()),
    path("timetable/section/<int:section_id>/", SectionReportAPIView.as_view()),
    path("timetable/teacher/<int:teacher_id>/", TeacherReportAPIView.as_view()),
    path("timetable/workload/", TeacherWorkloadAPIView.as_view()),

    path("timetable/drag/", TimetableDragAPIView.as_view()),
    path("timetable/update/", TimetableUpdateAPIView.as_view()),
    path("timetable/remove/", TimetableRemoveAPIView.as_view()),
]