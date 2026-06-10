from django.urls import (
    include,
    path,
)

urlpatterns = [

    # =====================================================
    # MASTERS
    # =====================================================

    path(
        "exam-types/",
        include(
            "apps.exams.exam_types.urls"
        ),
    ),

    path(
        "grade-scales/",
        include(
            "apps.exams.grade_scales.urls"
        ),
    ),

    path(
        "grade-calculations/",
        include(
            "apps.exams.grade_calculations.urls"
        ),
    ),

    path(
        "subject-configurations/",
        include(
            "apps.exams.subject_configurations.urls"
        ),
    ),

    path(
        "rank-systems/",
        include(
            "apps.exams.rank_systems.urls"
        ),
    ),

    path(
        "best-of-subjects/",
        include(
            "apps.exams.best_of_subjects.urls"
        ),
    ),

    # =====================================================
    # EXAM MANAGEMENT
    # =====================================================

    path(
        "exams/",
        include(
            "apps.exams.exams.urls"
        ),
    ),

    path(
        "date-sheets/",
        include(
            "apps.exams.date_sheets.urls"
        ),
    ),

    path(
        "seating-plans/",
        include(
            "apps.exams.seating_plans.urls"
        ),
    ),

    path(
        "admit-cards/",
        include(
            "apps.exams.admit_cards.urls"
        ),
    ),

    # =====================================================
    # ASSESSMENTS
    # =====================================================

    path(
        "mark-entries/",
        include(
            "apps.exams.mark_entries.urls"
        ),
    ),

    path(
        "mark-verifications/",
        include(
            "apps.exams.mark_verifications.urls"
        ),
    ),

    path(
        "internal-assessments/",
        include(
            "apps.exams.internal_assessments.urls"
        ),
    ),

    path(
        "practical-exams/",
        include(
            "apps.exams.practical_exams.urls"
        ),
    ),

    path(
        "competency-assessments/",
        include(
            "apps.exams.competency_assessments.urls"
        ),
    ),

    # =====================================================
    # RESULT PROCESSING
    # =====================================================

    path(
        "grace-marks/",
        include(
            "apps.exams.grace_marks.urls"
        ),
    ),

    path(
        "result-generations/",
        include(
            "apps.exams.result_generations.urls"
        ),
    ),

    path(
        "result-approvals/",
        include(
            "apps.exams.result_approvals.urls"
        ),
    ),

    path(
        "result-publications/",
        include(
            "apps.exams.result_publications.urls"
        ),
    ),

    path(
        "report-cards/",
        include(
            "apps.exams.report_cards.urls"
        ),
    ),

    # =====================================================
    # POST RESULT OPERATIONS
    # =====================================================

    path(
        "revaluations/",
        include(
            "apps.exams.revaluations.urls"
        ),
    ),

    path(
        "compartment-exams/",
        include(
            "apps.exams.compartment_exams.urls"
        ),
    ),

    path(
        "improvement-exams/",
        include(
            "apps.exams.improvement_exams.urls"
        ),
    ),

    # =====================================================
    # ANALYTICS & REPORTS
    # =====================================================

    path(
        "analytics/",
        include(
            "apps.exams.analytics.urls"
        ),
    ),

    path(
        "reports/",
        include(
            "apps.exams.reports.urls"
        ),
    ),
]