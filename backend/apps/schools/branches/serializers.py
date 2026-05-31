from rest_framework import serializers

from .models import Branch


class BranchSerializer(
    serializers.ModelSerializer
):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    class Meta:

        model = Branch

        fields = "__all__"