from django.urls import path, include

urlpatterns = [

    path(
        "post-types/",
        include(
            "apps.staff.post_type.urls"
        )
    ),

    path(
        "teacher-attendance/",
        include(
            "apps.staff.teacher_attendance.urls"
        )
    ),

    path(
        "staff/",
        include(
            "apps.staff.staff.urls"
        )
    ),

    path(
        "class-incharge/",
        include(
            "apps.staff.class_incharge.urls"
        )
    ),

    path(
        "sanctioned-post/",
        include(
            "apps.staff.sanctioned_post.urls"
        )
    ),
]