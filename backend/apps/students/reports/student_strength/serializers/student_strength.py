from rest_framework import serializers


class StudentStrengthSerializer(
    serializers.Serializer
):

    row_type = serializers.CharField()

    class_name = serializers.CharField()

    section_name = serializers.CharField()

    sc_male = serializers.IntegerField()
    sc_female = serializers.IntegerField()
    sc_total = serializers.IntegerField()

    bca_male = serializers.IntegerField()
    bca_female = serializers.IntegerField()
    bca_total = serializers.IntegerField()

    bcb_male = serializers.IntegerField()
    bcb_female = serializers.IntegerField()
    bcb_total = serializers.IntegerField()

    gen_male = serializers.IntegerField()
    gen_female = serializers.IntegerField()
    gen_total = serializers.IntegerField()

    overall_male = serializers.IntegerField()
    overall_female = serializers.IntegerField()
    overall_total = serializers.IntegerField()