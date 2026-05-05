from django.urls import path
from .views import *
from .views_extra import *
urlpatterns = [
    path("about/", AboutSchoolAPIView.as_view()),
    path("principal/", PrincipalAPIView.as_view()),
    path("affiliation/", AffiliationAPIView.as_view()),
    path("infrastructure/", InfrastructureAPIView.as_view()),
    path("disclosure/", MandatoryDisclosureAPIView.as_view()),
    path("faq/", FAQAPIView.as_view()),
    path("static/", StaticPagesAPIView.as_view()),
    path("contact/", ContactAPIView.as_view()),
    path("admission-form/", AdmissionFormAPIView.as_view()),
    path("pages/", WebsitePagesAPIView.as_view()),
    path("dashboard/", DashboardAPIView.as_view()),
]