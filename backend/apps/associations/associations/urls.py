# =============================================================================
# associations/urls/association_urls.py
# =============================================================================

from django.urls import path

from apps.associations.associations.views import (

    AssociationListAPIView,
    CommitteeDetailAPIView,
)

# =============================================================================
# APP NAME
# =============================================================================

app_name = "associations"

# =============================================================================
# URL PATTERNS
# =============================================================================

urlpatterns = [

    # ============================================
    # ASSOCIATION LIST
    # ============================================

    path(

        "",

        AssociationListAPIView.as_view(),

        name="association-list"
    ),

    # ============================================
    # COMMITTEE DETAIL
    # ============================================

    path(

        "committees/<int:pk>/",

        CommitteeDetailAPIView.as_view(),

        name="committee-detail"
    ),
]