from rest_framework import serializers

from apps.staff.sanctioned_posts.models import (
    SanctionedPost
)


class SanctionedPostSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True,
    )

    post_type_name = serializers.CharField(
        source="post_type.name",
        read_only=True,
    )

    regular_vacancy = serializers.IntegerField(
        read_only=True,
    )

    net_vacancy = serializers.IntegerField(
        read_only=True,
    )

    class Meta:

        model = SanctionedPost

        fields = [

            "id",

            "school",
            "school_name",

            "post_type",
            "post_type_name",

            "sanctioned_posts",

            "regular_working",
            "regular_vacancy",

            "guest_working",

            "hkrnl_working",

            "net_vacancy",
        ]

        read_only_fields = [

            "school_name",
            "post_type_name",
            "regular_vacancy",
            "net_vacancy",
        ]