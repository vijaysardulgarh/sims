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
        "users/",
        include("apps.users.urls")
    ),

    # ======================================
    # ACADEMICS
    # ======================================

    path(
        "academics/",
        include("apps.academics.urls")
    ),

    # ======================================
    # STAFF
    # ======================================

    path(
        "staff/",
        include("apps.staff.urls")
    ),

    # ======================================
    # STUDENTS API
    # ======================================

    path(

        "api/",

        include("apps.students.urls")
    ),

    # ======================================
    # FINANCE
    # ======================================

    path(
        "finance/",
        include("apps.finance.urls")
    ),

    path(
        "library/",
        include("apps.library.urls")
    ),

    # ======================================
    # ASSOCIATIONS
    # ======================================

    path(
        "associations/",
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
]