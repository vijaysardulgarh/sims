from rest_framework import serializers

from .models import Affiliation


class AffiliationSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(

        source="school.name",

        read_only=True
    )

    class Meta:

        model = Affiliation

        fields = "__all__"