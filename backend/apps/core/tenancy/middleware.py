from django.conf import settings

from django.http import JsonResponse

from apps.core.tenancy.tenant_resolver import (
    get_school_from_request
)


# ==========================================
# SCHOOL TENANT MIDDLEWARE
# ==========================================

class SchoolTenantMiddleware:

    def __init__(
        self,
        get_response
    ):

        self.get_response = get_response

    # ======================================
    # CALL
    # ======================================

    def __call__(
        self,
        request
    ):

        path = request.path

        host = request.get_host()

        # ==================================
        # SKIP SYSTEM PATHS
        # ==================================

        excluded_paths = [

            "/admin/",

            "/static/",

            "/media/",

            "/favicon.ico",
        ]

        if any(

            path.startswith(p)

            for p in excluded_paths
        ):

            return self.get_response(
                request
            )

        # ==================================
        # LOCALHOST SUPPORT
        # ==================================

        if (

            "localhost" in host

            or

            "127.0.0.1" in host
        ):

            request.school = None

            return self.get_response(
                request
            )

        # ==================================
        # GET SCHOOL
        # ==================================

        school = (
            get_school_from_request(
                request
            )
        )

        # ==================================
        # SCHOOL NOT FOUND
        # ==================================

        if not school:

            return JsonResponse(

                {

                    "success": False,

                    "message":
                    "Invalid school domain."
                },

                status=400
            )

        # ==================================
        # ATTACH SCHOOL
        # ==================================

        request.school = school

        # ==================================
        # CONTINUE
        # ==================================

        response = self.get_response(
            request
        )

        return response