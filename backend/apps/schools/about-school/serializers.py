from rest_framework import serializers

from .models import AboutSchool


class AboutSchoolSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = AboutSchool

        fields = "__all__"