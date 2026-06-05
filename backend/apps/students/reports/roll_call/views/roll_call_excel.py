from openpyxl import Workbook

from django.http import HttpResponse

from rest_framework.views import APIView

from apps.students.profiles.models import Student


class RollCallExcelAPIView(APIView):

    def get(self, request):

        school = request.user.school

        class_name = request.GET.get(
            "class"
        )

        section_name = request.GET.get(
            "section"
        )

        students = (
            Student.objects
            .filter(
                school=school,
                student_class__name=class_name,
                section__name=section_name,
            )
            .order_by(
                "roll_number"
            )
        )

        workbook = Workbook()

        sheet = workbook.active

        sheet.title = "Roll Call"

        headers = [

            "SRN",
            "Roll No",
            "Admission No",
            "Student Name",
            "Gender",
            "Father Name",
            "Mobile",
            "Category",

        ]

        sheet.append(headers)

        for student in students:

            sheet.append([

                student.srn,

                student.roll_number,

                student.admission_number,

                student.full_name_aadhar,

                student.gender,

                student.father_full_name_aadhar,

                student.father_mobile,

                student.category,

            ])

        response = HttpResponse(

            content_type=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            )

        )

        response[
            "Content-Disposition"
        ] = (
            f'attachment; filename="roll_call_{class_name}_{section_name}.xlsx"'
        )

        workbook.save(response)

        return response