from django.urls import path, include

urlpatterns = [

    path(
        "post-types/",
        include(
            "apps.staff.api.post_type.urls"
        )
    ),

    path(
        "teacher-attendance/",
        include(
            "apps.staff.api.teacher_attendance.urls"
        )
    ),

    path(
        "staff/",
        include(
            "apps.staff.api.staff.urls"
        )
    ),

    path(
        "class-incharge/",
        include(
            "apps.staff.api.class_incharge.urls"
        )
    ),

    path(
        "sanctioned-post/",
        include(
            "apps.staff.api.sanctioned_post.urls"
        )
    ),
]