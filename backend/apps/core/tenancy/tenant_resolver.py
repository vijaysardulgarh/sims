from apps.schools.models import (
    School
)


# ==========================================
# GET SCHOOL FROM REQUEST
# ==========================================

def get_school_from_request(
    request
):

    # ======================================
    # GET HOST
    # ======================================

    host = (
        request.get_host()
        .split(":")[0]
        .lower()
    )

    # ======================================
    # LOCALHOST SUPPORT
    # ======================================

    if host in [

        "localhost",

        "127.0.0.1"
    ]:

        return None

    # ======================================
    # DOMAIN PARTS
    # ======================================

    domain_parts = host.split(".")

    # ======================================
    # EXAMPLES
    # ======================================

    # school1.domain.com
    # school2.domain.com

    if len(domain_parts) < 3:

        return None

    # ======================================
    # SUBDOMAIN
    # ======================================

    subdomain = domain_parts[0]

    # ======================================
    # GET SCHOOL
    # ======================================

    try:

        return School.objects.get(

            slug=subdomain,

            is_active=True,

            is_deleted=False
        )

    except School.DoesNotExist:

        return None