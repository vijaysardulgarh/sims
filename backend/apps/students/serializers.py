from rest_framework import serializers

from apps.students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    student_class = serializers.SerializerMethodField()

    section = serializers.SerializerMethodField()

    stream = serializers.SerializerMethodField()

    medium = serializers.SerializerMethodField()

    school = serializers.SerializerMethodField()

    class Meta:

        model = Student

        fields = "__all__"

    # =====================================
    # CLASS
    # =====================================

    def get_student_class(self, obj):

        if obj.student_class:

            return {
                "name": obj.student_class.name
            }

        return None

    # =====================================
    # SECTION
    # =====================================

    def get_section(self, obj):

        if obj.section:

            return {
                "name": obj.section.name
            }

        return None

    # =====================================
    # STREAM
    # =====================================

    def get_stream(self, obj):

        if obj.stream:

            return {
                "name": obj.stream.name
            }

        return None

    # =====================================
    # MEDIUM
    # =====================================

    def get_medium(self, obj):

        if (

            obj.section and

            obj.section.medium
        ):

            return {
                "name": obj.section.medium.name
            }

        return None

    # =====================================
    # SCHOOL
    # =====================================

    def get_school(self, obj):

        if obj.school:

            return {
                "name": obj.school.name
            }

        return None