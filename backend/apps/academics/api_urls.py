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

from apps.academics.days.api import (
    DayViewSet
)

from apps.academics.timetable_slots.api import (
    TimetableSlotViewSet
)

from apps.academics.timetables.api import (
    TimetableViewSet
)

from apps.academics.timetable_generator.api import (
    TimetableGenerateAPIView
)

from apps.academics.teacher_subject_assignments.api import (
    TeacherAssignmentAPIView
)

from apps.academics.reports.teacher_workload.api import (
    TeacherWorkloadAPIView
)

# =========================================
# CLASS / STREAM / SECTION API IMPORTS
# =========================================

from apps.academics.classes.api import (
    ClassViewSet
)

from apps.academics.streams.api import (
    StreamViewSet
)

from apps.academics.mediums.api import (
    MediumViewSet
)

from apps.academics.classrooms.api import (
    ClassroomViewSet
)

from apps.academics.sections.api import (
    SectionViewSet
)

# =========================================
# SUBJECT API IMPORTS
# =========================================

from apps.academics.subjects.api import (
    SubjectViewSet
)

from apps.academics.class_subjects.api import (
    ClassSubjectViewSet
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
    # TEACHER WORKLOAD
    # =====================================

    path(
        "teacher-workload/",
        TeacherWorkloadAPIView.as_view(),
        name="teacher-workload"
    ),
]