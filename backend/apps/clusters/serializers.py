# =============================================================================
# clusters/serializers.py
# =============================================================================

from rest_framework import serializers

from apps.clusters.models import Cluster


class ClusterSerializer(
    serializers.ModelSerializer
):

    logo_url = serializers.SerializerMethodField()

    class Meta:

        model = Cluster

        fields = [

            "id",

            "name",

            "code",

            "slug",

            "description",

            "is_active",

            "logo",

            "logo_url",

            "email",

            "phone",

            "address",

            "timezone",

            "currency",

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