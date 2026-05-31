from django.contrib import admin

from django.urls import path, include


# ==========================================
# MASTER API ROUTER
# ==========================================

urlpatterns = [

    # ======================================
    # DJANGO ADMIN
    # ======================================

    path(
        "admin/",
        admin.site.urls
    ),

    # ======================================
    # USERS / AUTH
    # ======================================

    path(
        "api/accounts/",
        include("apps.accounts.urls")
    ),

    # ======================================
    # ACADEMICS
    # ======================================

    path(
        "api/academics/",
        include("apps.academics.urls")
    ),

    # ======================================
    # STAFF
    # ======================================

    path(
        "api/staff/",
        include("apps.staff.urls")
    ),

    # ======================================
    # STUDENTS API
    # ======================================

    path(

        "api/students/",

        include("apps.students.urls")
    ),

    # ======================================
    # FINANCE
    # ======================================

    path(
        "api/finance/",
        include("apps.finance.urls")
    ),

    path(
        "api/library/",
        include("apps.library.urls")
    ),

    # ======================================
    # ASSOCIATIONS
    # ======================================

    path(
        "api/associations/",
        include("apps.associations.urls")
    ),

    # ======================================
    # WEBSITE APIs
    # ======================================

    path(
        "api/website/",
        include("apps.website.urls")
    ),

    path(
        "api/documents/",
        include("apps.documents.urls")
    ),

    path(
        "api/finance/",
        include("apps.finance.urls")
    ),

    path(
        "api/schools/",
        include("apps.schools.urls")
    ),
    path(
        "api/clusters/",
        include("apps.clusters.urls")
    ),

    path(
        "api/infrastructure/",
        include("apps.infrastructure.urls")
    ),

    path(
        "api/compliance/",
        include("apps.compliance.urls")
    ),
    path(
        "api/communications/",
        include("apps.communications.urls")
    ),
]