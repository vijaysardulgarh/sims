# =============================================================================
# apps/associations/urls.py
# =============================================================================

from django.urls import (
    include,
    path,
)

urlpatterns = [

    # =========================================================================
    # ASSOCIATIONS
    # =========================================================================

    path(

        "associations/",

        include(
            "apps.associations.associations.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION ROLES
    # =========================================================================

    path(

        "association-roles/",

        include(
            "apps.associations.association_roles.urls"
        )
    ),


    path(
        "association-role-assignments/",
        include(
            "apps.associations.association_role_assignments.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION MEMBERS
    # =========================================================================

    path(

        "association-members/",

        include(
            "apps.associations.association_members.urls"
        )
    ),

    # =========================================================================
    # ASSOCIATION MEETINGS
    # =========================================================================

    path(

        "association-meetings/",

        include(
            "apps.associations.association_meetings.urls"
        )
    ),

    # =========================================================================
    # SCHOOL MANAGEMENT COMMITTEE MEMBERS
    # =========================================================================

    path(

        "smc-members/",

        include(
            "apps.associations.smc_members.urls"
        )
    ),

    # =========================================================================
    # EXTRACURRICULAR ACTIVITIES
    # =========================================================================

    path(

        "extracurricular-activities/",

        include(
            "apps.associations.extracurricular_activities.urls"
        )
    ),
]