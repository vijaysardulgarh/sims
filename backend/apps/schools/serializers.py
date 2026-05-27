# =============================================================================
# schools/serializers.py
# =============================================================================

from rest_framework import serializers

from apps.schools.models import School


class SchoolSerializer(
    serializers.ModelSerializer
):

    logo_url = serializers.SerializerMethodField()

    cluster_name = serializers.CharField(
        source="cluster.name",
        read_only=True
    )

    class Meta:

        model = School

        fields = [

            "id",

            "cluster",

            "cluster_name",

            "name",

            "code",

            "slug",

            "subdomain",

            "motto",

            "is_active",

            "logo",

            "logo_url",

            "email",

            "phone",

            "alternate_phone",

            "website",

            "address",

            "city",

            "state",

            "country",

            "pincode",

            "principal_name",

            "established_date",

            "accreditation",

            "affiliation_number",

            "school_type",

            "board",

            "language",

            "academic_year_start_month",

            "timezone",

            "currency",

            "social_media_links",

            "latitude",

            "longitude",

            "geo_radius_meters",

            "created_at",

            "updated_at",
        ]

        read_only_fields = [

            "slug",

            "created_at",

            "updated_at",
        ]

    def get_logo_url(
        self,
        obj
    ):

        request = self.context.get(
            "request"
        )

        if (
            obj.logo and
            request
        ):

            return request.build_absolute_uri(
                obj.logo.url
            )

        return None