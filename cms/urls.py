from django.urls import path
from . import views
from .views import timetable_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("school/<int:school_id>/documents/", views.document_detail, name="document_detail"),

    # Home
    path('', views.index, name='index'),

    # About Us
    path('about/', views.about_school, name='about'),
    path('principal/', views.principal, name='principal_message'),
    path('committee/', views.committee, name='committee'),
    path("nodal/", views.nodal, name="nodal"),
    #path('nodal', views.nodal, name='nodal_detail'),
    #path("nodals/", views.nodal_list, name="nodal_list"),
    # path("nodals/<int:pk>/", views.nodal_detail, name="nodal_detail"),
    path('affiliation/', views.affiliation_status, name='affiliation_status'),
    path("infrastructure/", views.infrastructure, name="infrastructure"),
    #path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('smc_members/', views.smc_members, name='smc_members'),
    path("staff/associations/", views.staff_association_roles, name="staff_association_roles"),

    # Academics
    path("subjects_offered/", views.subjects_offered, name="subjects"),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('academics/syllabus/', views.syllabus, name='syllabus'),
    path('academics/exams/', views.exams_results, name='exams'),
    path('academics/calendar/', views.academic_calendar, name='calendar'),
    path('academics/timetable/', views.time_table, name='time_table'),
    path('academics/downloads/', views.downloads, name='downloads'),

    # Staff
    path('staff/admin/', views.admin_staff, name='admin_staff'),
    path('staff/teaching/', views.teaching_staff, name='teaching_staff'),
    path('staff/nonteaching/', views.non_teaching_staff, name='non_teaching_staff'),
    path('staff/support/', views.support_staff, name='support_staff'),
    path('staff/<str:role>/', views.staff_by_role, name='staff_by_role'),

    # Committees
    path('committees/', views.committee_list, name='committee_list'),
    path('committees/<int:pk>/', views.committee_detail, name='committee_detail'),

    # Statistics
    path('staff_summary/', views.staff_summary, name='staff_summary'),
    path('student_strength/', views.student_strength, name='student_strength'),
    path('subject_strength/', views.subject_strength, name='subject_strength'),
    path('school_subject_strength/', views.subject_strength, name='school_subject_strength'),


    # Timetable
    path('timetable/', timetable_view, name='timetable'),

    # Students
    path("achievements/", views.achievement_list, name="achievement_list"),
    path("achievements/<int:pk>/", views.achievement_detail, name="achievement_detail"),
    path('students/achievements/', views.achievements, name='achievements'),
    path('students/results/', views.board_results, name='board_results'),
    path('students/sports/', views.sports_achievements, name='sports_achievements'),
    path('students/gallery/', views.gallery, name='gallery'),
    path('students/notices/', views.notices, name='notices'),
    path('students/events/', views.events, name='events'),

    # Admissions
    path('admission_procedure/', views.admission_procedure, name='admission_procedure'),
    path('admission_form/', views.admission_form, name='admission_form'),
    path('admissions/prospectus/', views.prospectus, name='prospectus'),
    path("fees/", views.fee_structure_list, name="fee_structure_list"),
    #path('fee_structure/', views.fee_structure, name='fee_structure'),
    path('faq', views.faq, name='faq'),

    # Mandatory Info
    path('mandatory/disclosure/', views.mandatory_disclosure, name='mandatory_disclosure'),
    path("committee/<int:pk>/", views.committee_detail, name="committee_detail"),
    # path('mandatory/statistics/', views.statistics, name='statistics'),
    # path('mandatory/safety/', views.safety_committee, name='safety_committee'),
    # path('mandatory/grievance/', views.grievance_committee, name='grievance_committee'),
    # path('mandatory/icc/', views.icc_committee, name='icc_committee'),

    # Contact
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

