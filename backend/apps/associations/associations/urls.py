# =============================================================================
# associations/urls/association_urls.py
# =============================================================================

from django.urls import path

from apps.associations.associations.views import (
    AssociationListAPIView,
    AssociationDetailAPIView,
)

# =============================================================================
# APP NAME
# =============================================================================

app_name = "associations"

# =============================================================================
# URL PATTERNS
# =============================================================================

urlpatterns = [

    # =========================================================
    # LIST + CREATE
    # =========================================================

    path(
        "",
        AssociationListAPIView.as_view(),
        name="association-list"
    ),

    # =========================================================
    # DETAIL + UPDATE + DELETE
    # =========================================================

    path(
        "<int:pk>/",
        AssociationDetailAPIView.as_view(),
        name="association-detail"
    ),

]