from django.urls import path

from .views import (

    PublishTimetableView,
    CompareVersionView,

)

urlpatterns = [

    path(
        "publish/",
        PublishTimetableView.as_view()
    ),

    path(
        "compare/",
        CompareVersionView.as_view()
    ),

]