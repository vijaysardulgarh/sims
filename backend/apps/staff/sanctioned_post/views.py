from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum, Q

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.staff.profiles.models import (
    Staff,
)
from apps.staff.sanctioned_post.models import (
    SanctionedPost
)

from apps.schools.models import School


class StaffSummaryAPIView(APIView):

    def get(self, request):

        school_id = request.session.get(
            "school_id"
        )

        school = get_object_or_404(
            School,
            id=school_id
        )

        allowed = [
            "Principal",
            "PGT",
            "TGT",
            "Clerk",
            "Lab Attendent",
            "Class IV"
        ]

        sanctioned = (
            SanctionedPost.objects
            .filter(
                school=school,
                post_type__name__in=allowed
            )
            .values(
                "post_type__name",
                "subject__name"
            )
            .annotate(
                sanctioned_posts=Sum("total_posts")
            )
        )

        sanctioned_map = {

            (
                r["post_type__name"],
                r["subject__name"]
            ): r["sanctioned_posts"]

            for r in sanctioned
        }

        staff_data = (
            Staff.objects
            .filter(
                school=school,
                post_type__name__in=allowed
            )
            .values(
                "post_type__name",
                "subject__name"
            )
            .annotate(
                regular=Count(
                    "id",
                    filter=Q(
                        employment_type="Regular"
                    )
                ),

                guest=Count(
                    "id",
                    filter=Q(
                        employment_type="Guest"
                    )
                ),

                hkrnl=Count(
                    "id",
                    filter=Q(
                        employment_type="HKRNL"
                    )
                ),

                male=Count(
                    "id",
                    filter=Q(
                        gender="Male"
                    )
                ),

                female=Count(
                    "id",
                    filter=Q(
                        gender="Female"
                    )
                ),
            )
        )

        staff_map = {

            (
                r["post_type__name"],
                r["subject__name"]
            ): r

            for r in staff_data
        }

        result = []

        for key, sanctioned_posts in sanctioned_map.items():

            post, subject = key

            s = staff_map.get(key, {})

            row = {
                "post": post,
                "subject": subject,
                "sanctioned": sanctioned_posts,
                "regular": s.get("regular", 0),
                "guest": s.get("guest", 0),
                "hkrnl": s.get("hkrnl", 0),
                "male": s.get("male", 0),
                "female": s.get("female", 0),
            }

            row["vacant"] = (
                sanctioned_posts - row["regular"]
            )

            row["net_vacancy"] = (
                sanctioned_posts
                - row["regular"]
                - row["guest"]
                - row["hkrnl"]
            )

            result.append(row)

        return Response(result)