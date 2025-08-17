from django.urls import path
from . import views
from .views import timetable_view
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.about,name='contact'),
    #path('staff_members',views.staff,name='staff_members'),
    path('student_strength',views.student_strength,name='student_strength'),
    path('subject_strength',views.subject_strength,name='subject_strength'),
    #path('school_subject_strength',views.student_strength,name='school_subject_strength'),
    path('timetable/', timetable_view, name='timetable'),
    path("staff/<str:role>/", views.staff_by_role, name="staff_by_role"),
  
]



