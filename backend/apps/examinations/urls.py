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
            "apps.examinations.exam_types.urls"
        ),
    ),

    path(
        "grade-scales/",
        include(
            "apps.examinations.grade_scales.urls"
        ),
    ),

    path(
        "grade-calculations/",
        include(
            "apps.examinations.grade_calculations.urls"
        ),
    ),

    path(
        "subject-configurations/",
        include(
            "apps.examinations.subject_configurations.urls"
        ),
    ),

    path(
        "rank-systems/",
        include(
            "apps.examinations.rank_systems.urls"
        ),
    ),

    path(
        "best-of-subjects/",
        include(
            "apps.examinations.best_of_subjects.urls"
        ),
    ),

    # =====================================================
    # EXAM MANAGEMENT
    # =====================================================

    path(
        "exams/",
        include(
            "apps.examinations.exams.urls"
        ),
    ),

    path(
        "date-sheets/",
        include(
            "apps.examinations.date_sheets.urls"
        ),
    ),

    path(
        "seating-plans/",
        include(
            "apps.examinations.seating_plans.urls"
        ),
    ),

    path(
        "admit-cards/",
        include(
            "apps.examinations.admit_cards.urls"
        ),
    ),

    # =====================================================
    # ASSESSMENTS
    # =====================================================

    path(
        "mark-entries/",
        include(
            "apps.examinations.mark_entries.urls"
        ),
    ),

    path(
        "mark-verifications/",
        include(
            "apps.examinations.mark_verifications.urls"
        ),
    ),

    path(
        "internal-assessments/",
        include(
            "apps.examinations.internal_assessments.urls"
        ),
    ),

    path(
        "practical-exams/",
        include(
            "apps.examinations.practical_exams.urls"
        ),
    ),

    path(
        "competency-assessments/",
        include(
            "apps.examinations.competency_assessments.urls"
        ),
    ),

    # =====================================================
    # RESULT PROCESSING
    # =====================================================

    path(
        "grace-marks/",
        include(
            "apps.examinations.grace_marks.urls"
        ),
    ),

    path(
        "result-generations/",
        include(
            "apps.examinations.result_generations.urls"
        ),
    ),

    path(
        "result-approvals/",
        include(
            "apps.examinations.result_approvals.urls"
        ),
    ),

    path(
        "result-publications/",
        include(
            "apps.examinations.result_publications.urls"
        ),
    ),

    path(
        "report-cards/",
        include(
            "apps.examinations.report_cards.urls"
        ),
    ),

    # =====================================================
    # POST RESULT OPERATIONS
    # =====================================================

    path(
        "revaluations/",
        include(
            "apps.examinations.revaluations.urls"
        ),
    ),

    path(
        "compartment-exams/",
        include(
            "apps.examinations.compartment_exams.urls"
        ),
    ),

    path(
        "improvement-exams/",
        include(
            "apps.examinations.improvement_exams.urls"
        ),
    ),

    # =====================================================
    # ANALYTICS & REPORTS
    # =====================================================

    path(
        "analytics/",
        include(
            "apps.examinations.analytics.urls"
        ),
    ),

    path(
        "reports/",
        include(
            "apps.examinations.reports.urls"
        ),
    ),
]