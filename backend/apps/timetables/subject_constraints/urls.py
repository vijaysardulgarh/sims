from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectConstraintViewSet

router = DefaultRouter()
router.register(r'', SubjectConstraintViewSet, basename='subject-constraint')

urlpatterns = [
    path('bulk_assign/', SubjectConstraintViewSet.as_view({
        'get': 'bulk_assign',
        'post': 'bulk_assign'
    }), name='subject-constraint-bulk-assign'),
    path('', include(router.urls)),
]