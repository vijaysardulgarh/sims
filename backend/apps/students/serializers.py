from rest_framework import serializers

from apps.students.models import Student


class StudentSerializer(
    serializers.ModelSerializer
):

    # =====================================
    # DISPLAY FIELDS
    # =====================================

    student_class_data = (
        serializers.SerializerMethodField()
    )

    section_data = (
        serializers.SerializerMethodField()
    )

    stream_data = (
        serializers.SerializerMethodField()
    )

    medium_data = (
        serializers.SerializerMethodField()
    )

    school_data = (
        serializers.SerializerMethodField()
    )

    # =====================================
    # META
    # =====================================

    class Meta:

        model = Student

        fields = "__all__"

        read_only_fields = [
            "school"
        ]

    # =====================================
    # CLASS
    # =====================================

    def get_student_class_data(
        self,
        obj
    ):

        if obj.student_class:

            return {

                "id":
                    obj.student_class.id,

                "name":
                    obj.student_class.name,
            }

        return None

    # =====================================
    # SECTION
    # =====================================

    def get_section_data(
        self,
        obj
    ):

        if obj.section:

            return {

                "id":
                    obj.section.id,

                "name":
                    obj.section.name,
            }

        return None

    # =====================================
    # STREAM
    # =====================================

    def get_stream_data(
        self,
        obj
    ):

        if obj.stream:

            return {

                "id":
                    obj.stream.id,

                "name":
                    obj.stream.name,
            }

        return None

    # =====================================
    # MEDIUM
    # =====================================

    def get_medium_data(
        self,
        obj
    ):

        if (

            obj.section and

            obj.section.medium
        ):

            return {

                "id":
                    obj.section.medium.id,

                "name":
                    obj.section.medium.name,
            }

        return None

    # =====================================
    # SCHOOL
    # =====================================

    def get_school_data(
        self,
        obj
    ):

        if obj.school:

            return {

                "id":
                    obj.school.id,

                "name":
                    obj.school.name,
            }

        return None