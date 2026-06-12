from django.urls import path

from .views import (

    GenerateTimetableView,
    MoveEntryView,
    CopyDayView,
    CopyWeekView,
    PublishTimetableView,
    ConflictCheckView,
    TeacherView,
    RoomView,
    ClassView,
    CompareVersionView,

    TimetableGridView,
    AssignSubjectView,
    AssignTeacherView,
    AssignRoomView,

)

urlpatterns = [

    path(
        "generate/",
        GenerateTimetableView.as_view()
    ),

    path(
        "move-entry/",
        MoveEntryView.as_view()
    ),

    path(
        "copy-day/",
        CopyDayView.as_view()
    ),

    path(
        "copy-week/",
        CopyWeekView.as_view()
    ),

    path(
        "publish/",
        PublishTimetableView.as_view()
    ),

    path(
        "conflicts/",
        ConflictCheckView.as_view()
    ),

    path(
        "teacher-view/<int:teacher_id>/",
        TeacherView.as_view()
    ),

    path(
        "room-view/<int:room_id>/",
        RoomView.as_view()
    ),

    path(
        "class-view/<int:class_id>/",
        ClassView.as_view()
    ),

    path(
        "compare/",
        CompareVersionView.as_view()
    ),

    # =====================================================
    # TIMETABLE DESIGNER
    # =====================================================

    path(
        "grid/<int:timetable_id>/",
        TimetableGridView.as_view()
    ),

    path(
        "assign-subject/",
        AssignSubjectView.as_view()
    ),

    path(
        "assign-teacher/",
        AssignTeacherView.as_view()
    ),

    path(
        "assign-room/",
        AssignRoomView.as_view()
    ),

]