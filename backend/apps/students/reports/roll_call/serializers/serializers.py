from rest_framework import serializers

from apps.students.profiles.models import Student


class RollCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        fields = [
            "srn",
            "roll_number",
            "admission_number",
            "full_name_aadhar",
            "date_of_birth",
            "gender",
            "aadhaar_number",
            "father_full_name_aadhar",
            "mother_full_name_aadhar",
            "father_mobile",
            "category",
        ]