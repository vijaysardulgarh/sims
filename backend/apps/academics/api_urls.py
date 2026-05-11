from django.urls import (
    path,
    include,
)

from rest_framework.routers import (
    DefaultRouter
)

# =========================================
# TIMETABLE API IMPORTS
# =========================================

from apps.academics.api.timetable_api import (

    DayViewSet,

    TimetableSlotViewSet,

    TimetableViewSet,

    TimetableGenerateAPIView,

    TeacherAssignmentAPIView,

    TimetableListAPIView,

    TeacherWorkloadAPIView,
)

# =========================================
# CLASS / STREAM / SECTION API IMPORTS
# =========================================

from apps.academics.api.class_api import (

    ClassViewSet,

    StreamViewSet,

    MediumViewSet,

    ClassroomViewSet,

    SectionViewSet,
)

# =========================================
# ROUTER
# =========================================

router = DefaultRouter()

# =========================================
# TIMETABLE ROUTES
# =========================================

router.register(
    r"days",
    DayViewSet
)

router.register(
    r"timetable-slots",
    TimetableSlotViewSet
)

router.register(
    r"timetable",
    TimetableViewSet
)

# =========================================
# CLASS ROUTES
# =========================================

router.register(
    r"classes",
    ClassViewSet
)

# =========================================
# STREAM ROUTES
# =========================================

router.register(
    r"streams",
    StreamViewSet
)

# =========================================
# MEDIUM ROUTES
# =========================================

router.register(
    r"mediums",
    MediumViewSet
)

# =========================================
# CLASSROOM ROUTES
# =========================================

router.register(
    r"classrooms",
    ClassroomViewSet
)

# =========================================
# SECTION ROUTES
# =========================================

router.register(
    r"sections",
    SectionViewSet
)

# =========================================
# URLPATTERNS
# =========================================

urlpatterns = [

    # =====================================
    # ROUTER URLS
    # =====================================

    path(
        "",
        include(router.urls)
    ),

    # =====================================
    # TIMETABLE GENERATE
    # =====================================

    path(
        "generate/",
        TimetableGenerateAPIView.as_view()
    ),

    # =====================================
    # TEACHER ASSIGNMENT
    # =====================================

    path(
        "teacher-assignment/",
        TeacherAssignmentAPIView.as_view()
    ),

    # =====================================
    # TIMETABLE LIST
    # =====================================

    path(
        "timetable-list/",
        TimetableListAPIView.as_view()
    ),

    # =====================================
    # TEACHER WORKLOAD
    # =====================================

    path(
        "teacher-workload/",
        TeacherWorkloadAPIView.as_view()
    ),
]