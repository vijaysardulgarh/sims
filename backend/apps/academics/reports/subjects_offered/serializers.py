from rest_framework import serializers


# =========================================
# SUBJECT OFFERED ITEM SERIALIZER
# =========================================

class SubjectOfferedItemSerializer(
    serializers.Serializer
):

    subject = serializers.CharField()

    periods_per_week = serializers.IntegerField()

    is_optional = serializers.BooleanField()

    has_lab = serializers.BooleanField()


# =========================================
# SUBJECTS OFFERED SERIALIZER
# =========================================

class SubjectsOfferedSerializer(
    serializers.Serializer
):

    class_name = serializers.CharField()

    subjects = (
        SubjectOfferedItemSerializer(
            many=True
        )
    )