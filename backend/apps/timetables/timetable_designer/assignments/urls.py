from django.urls import path

from .views import (

    AssignSubjectView,
    AssignTeacherView,
    AssignRoomView,

)

urlpatterns = [

    path(
        "subject/",
        AssignSubjectView.as_view()
    ),

    path(
        "teacher/",
        AssignTeacherView.as_view()
    ),

    path(
        "room/",
        AssignRoomView.as_view()
    ),

]