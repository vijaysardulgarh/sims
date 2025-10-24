from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import timetable_dragndrop
from cms.admin.admin import timetable_admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import cbse_enrollment_csv, cbse_enrollment_pdf
urlpatterns = [
    #path('dashboard/', views.dashboard, name='dashboard'),
    path('cbse/enrollment/csv/', cbse_enrollment_csv, name='cbse_enrollment_csv'),
    path('cbse/enrollment/pdf/', cbse_enrollment_pdf, name='cbse_enrollment_pdf'),
    path('timetable_dragndrop/', views.timetable_dragndrop, name='timetable_dragndrop'),
    path('timetable_update/', views.timetable_update, name='timetable_update'),
    path('timetable_remove/', views.timetable_remove, name='timetable_remove'),
    path('', views.sims_index, name='sims_index'),    # Home page → sims_index.html
    path('index/', views.index, name='index'),   # index.html page
    path("timetable-admin/", timetable_admin.urls),
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True, next_page='/index/'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="sims_index"), name="logout"),
    #path("accounts/", include("django.contrib.auth.urls")),  # 👈 includes login/logout
    # Home
    path('timetable/create/', views.create_timetable_entry, name='create_timetable_entry'),
    path('timetable/', views.timetable_list, name='timetable_list'),  # optional: list all timetable entries
    path('teacher-subject-section-assignment/', views.teacher_subject_section_assignment, name='teacher_subject_section_assignment'),
    path('ajax/get_subjects/', views.get_subjects_for_section, name='get_subjects_for_section'),
    # About
    path('about/', views.about_school, name='about'),
    path('principal/', views.principal, name='principal_message'),
    path('committee/', views.committee, name='committee'),
    path('nodal/', views.nodal, name='nodal'),
    path('affiliation/', views.affiliation_status, name='affiliation_status'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('smc_members/', views.smc_members, name='smc_members'),
    path('staff/associations/', views.staff_association_roles, name='staff_association_roles'),

    # Academics
    path('subjects_offered/', views.subjects_offered, name='subjects'),
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
    #path('timetable/', timetable_view, name='timetable'),

    # Students
    path('achievements/', views.achievement_list, name='achievement_list'),
    path('achievements/<int:pk>/', views.achievement_detail, name='achievement_detail'),
    path('students/achievements/', views.achievements, name='achievements'),
    path('students/results/', views.board_results, name='board_results'),
    path('students/sports/', views.sports_achievements, name='sports_achievements'),
    path('students/gallery/', views.gallery, name='gallery'),
    path('students/notices/', views.notices, name='notices'),
    path('students/events/', views.events, name='events'),
    path('signin/<str:class_name>/<str:section_name>/', views.signin, name='signin'),
    path("reports/cwsn/", views.cwsn_students_report, name="cwsn_students_report"),
    path("reports/bpl/", views.bpl_students_report, name="bpl_students_report"),
    #path("roll-call/<str:studentclass>/<str:section>/", views.roll_call, name="roll_call"),
    
    path('roll-call/<str:class_name>/<str:section_name>/', views.roll_call, name='roll_call'),
    path('signin_link/', views.signin_link, name='signin_link'),
    path('roll_call_link/', views.roll_call_link, name='roll_call_link'),
    path('student-strength-pdf/', views.generate_student_strength_pdf, name='student_strength_pdf'),
        # ✅ Subject Reports
    path("subject-report/", views.subject_report_link, name="subject_report_link"),
    path("subject-report/<str:class_name>/<str:section_name>/", views.subject_report, name="subject_report"),
    path("reports/class-incharge/", views.class_incharge_report, name="class_incharge_report"),
    # Bank Report
    path("bank-report/", views.bank_report_link, name="bank_report_link"),
    path("bank-report/<str:class_name>/<str:section_name>/", views.bank_report, name="bank_report"),
    path("reports/", views.reports_dashboard, name="reports_dashboard"),
    path("attendance/", views.teacher_attendance, name="teacher_attendance"),
    path("attendance/update/<int:pk>/", views.teacher_attendance_update, name="teacher_attendance_update"),
    path("attendance/delete/<int:pk>/", views.teacher_attendance_delete, name="teacher_attendance_delete"),
    # Admissions & Fees
    path('admission_procedure/', views.admission_procedure, name='admission_procedure'),
    path('admission_form/', views.admission_form, name='admission_form'),
    path('admissions/prospectus/', views.prospectus, name='prospectus'),
    path('fees/', views.fee_structure_list, name='fee_structure_list'),

    # FAQ & Contact
    path('faq/', views.faq, name='faq'),
    path('mandatory_public_disclosure/', views.mandatory_public_disclosure, name='mandatory_public_disclosure'),
    path('contact/', views.contact, name='contact'),

    # School Documents
    path('school/<int:school_id>/documents/', views.document_detail, name='document_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
