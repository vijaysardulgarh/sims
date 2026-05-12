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
# SUBJECT API IMPORTS
# =========================================

from apps.academics.api.subject_api import (

    SubjectViewSet,

    ClassSubjectViewSet,
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
    DayViewSet,
    basename="days"
)

router.register(
    r"timetable-slots",
    TimetableSlotViewSet,
    basename="timetable-slots"
)

router.register(
    r"timetable",
    TimetableViewSet,
    basename="timetable"
)

# =========================================
# CLASS ROUTES
# =========================================

router.register(
    r"classes",
    ClassViewSet,
    basename="classes"
)

# =========================================
# STREAM ROUTES
# =========================================

router.register(
    r"streams",
    StreamViewSet,
    basename="streams"
)

# =========================================
# MEDIUM ROUTES
# =========================================

router.register(
    r"mediums",
    MediumViewSet,
    basename="mediums"
)

# =========================================
# CLASSROOM ROUTES
# =========================================

router.register(
    r"classrooms",
    ClassroomViewSet,
    basename="classrooms"
)

# =========================================
# SECTION ROUTES
# =========================================

router.register(
    r"sections",
    SectionViewSet,
    basename="sections"
)

# =========================================
# SUBJECT ROUTES
# =========================================

router.register(
    r"subjects",
    SubjectViewSet,
    basename="subjects"
)

# =========================================
# CLASS SUBJECT ROUTES
# =========================================

router.register(
    r"class-subjects",
    ClassSubjectViewSet,
    basename="class-subjects"
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
        TimetableGenerateAPIView.as_view(),
        name="generate-timetable"
    ),

    # =====================================
    # TEACHER ASSIGNMENT
    # =====================================

    path(
        "teacher-assignment/",
        TeacherAssignmentAPIView.as_view(),
        name="teacher-assignment"
    ),

    # =====================================
    # TIMETABLE LIST
    # =====================================

    path(
        "timetable-list/",
        TimetableListAPIView.as_view(),
        name="timetable-list"
    ),

    # =====================================
    # TEACHER WORKLOAD
    # =====================================

    path(
        "teacher-workload/",
        TeacherWorkloadAPIView.as_view(),
        name="teacher-workload"
    ),
]