from django.contrib import admin

from django.urls import (
    path,
    include
)

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [

    # =====================================
    # DJANGO ADMIN
    # =====================================

    path(
        "admin/",
        admin.site.urls
    ),

    # =====================================
    # USERS API
    # =====================================

    path(
        "api/users/",
        include(
            "apps.users.urls"
        )
    ),

]


# =====================================
# MEDIA FILES
# =====================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )