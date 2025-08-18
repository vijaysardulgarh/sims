from django.urls import path
from . import views
from .views import timetable_view
from django.conf import settings
from django.conf.urls.static import static
import os
urlpatterns = [
    path("school/<int:school_id>/documents/", views.document_detail, name="document_detail"),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.about,name='contact'),
    #path('staff_members',views.staff,name='staff_members'),
    path('student_strength',views.student_strength,name='student_strength'),
    path('smc_members',views.smc_members,name='smc_members'),
    path('subject_strength',views.subject_strength,name='subject_strength'),
    #path('school_subject_strength',views.student_strength,name='school_subject_strength'),
    path('timetable/', timetable_view, name='timetable'),
    path("staff/<str:role>/", views.staff_by_role, name="staff_by_role"),
  
]


if settings.DEBUG:
    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve static files (including admin CSS/JS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


