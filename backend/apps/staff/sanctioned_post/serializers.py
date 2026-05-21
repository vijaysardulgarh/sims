from rest_framework import serializers

from apps.staff.sanctioned_post.models import SanctionedPost


class SanctionedPostSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    post_type_name = serializers.CharField(
        source="post_type.name",
        read_only=True
    )

    subject_name = serializers.CharField(
        source="subject.name",
        read_only=True
    )

    class Meta:

        model = SanctionedPost

        fields = [
            "id",
            "school",
            "school_name",
            "post_type",
            "post_type_name",
            "designation",
            "subject",
            "subject_name",
            "total_posts",
        ]