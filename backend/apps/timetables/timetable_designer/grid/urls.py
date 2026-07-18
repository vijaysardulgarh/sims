from django.urls import path

from .views import (

    TimetableGridView,
    TeacherView,
    RoomView,
    ClassView,

)

urlpatterns = [

    path(
        "<int:timetable_id>/",
        TimetableGridView.as_view()
    ),

    path(
        "teacher/<int:teacher_id>/",
        TeacherView.as_view()
    ),

    path(
        "room/<int:room_id>/",
        RoomView.as_view()
    ),

    path(
        "class/<int:class_id>/",
        ClassView.as_view()
    ),

]