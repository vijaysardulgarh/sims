from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from django.http import HttpResponse

from tablib import Dataset

from apps.students.student_resource import (
    StudentResource
)

# =========================================
# IMPORT STUDENTS
# =========================================

class StudentImportAPIView(APIView):

    parser_classes = (
        MultiPartParser,
        FormParser
    )

    def post(self, request):

        file = request.FILES.get("file")

        if not file:

            return Response({

                "success": False,

                "error":
                    "No file uploaded"

            }, status=400)

        try:

            dataset = Dataset()

            imported_data = dataset.load(

                file.read(),

                format="xlsx"
            )

            resource = StudentResource()

            result = resource.import_data(

                imported_data,

                dry_run=False,

                raise_errors=False
            )

            return Response({

                "success": True,

                "message":
                    "Students imported successfully",

                "total_rows":
                    len(imported_data),

                "invalid_rows":
                    len(result.invalid_rows),

                "errors":
                    len(result.row_errors()),
            })

        except Exception as e:

            return Response({

                "success": False,

                "error": str(e)

            }, status=400)
        
# =========================================
# EXPORT STUDENTS
# =========================================

class StudentExportAPIView(APIView):

    def get(self, request):

        resource = StudentResource()

        dataset = resource.export()

        response = HttpResponse(

            dataset.xlsx,

            content_type=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            )
        )

        response[
            "Content-Disposition"
        ] = (
            'attachment; filename="students.xlsx"'
        )

        return response        