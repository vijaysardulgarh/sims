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

        print("\n====================")
        print("IMPORT API CALLED")
        print("====================\n")

        file = request.FILES.get("file")

        # =========================================
        # FILE REQUIRED
        # =========================================

        if not file:

            print("NO FILE RECEIVED")

            return Response({

                "success": False,

                "error":
                    "No file uploaded"

            }, status=400)

        try:

            # =========================================
            # FILE INFO
            # =========================================

            print("FILE NAME:", file.name)

            file_format = (
                file.name
                .split(".")[-1]
                .lower()
            )

            print("FILE FORMAT:", file_format)

            # =========================================
            # ALLOWED FORMATS
            # =========================================

            allowed_formats = [
                "xlsx",
                "xls",
                "csv"
            ]

            if file_format not in allowed_formats:

                print("INVALID FILE FORMAT")

                return Response({

                    "success": False,

                    "error":
                        "Only xlsx, xls and csv files are allowed"

                }, status=400)

            # =========================================
            # LOAD DATASET
            # =========================================

            dataset = Dataset()

            imported_data = dataset.load(

                file.read(),

                format=file_format
            )

            print(
                "ROWS FOUND:",
                len(imported_data)
            )

            # =========================================
            # IMPORT RESOURCE
            # =========================================

            resource = StudentResource()

            result = resource.import_data(

                imported_data,

                dry_run=False,

                raise_errors=False
            )

            print("IMPORT SUCCESS")

            # =========================================
            # SHOW ERRORS IF ANY
            # =========================================

            if result.has_errors():

                print("\n====================")
                print("ROW ERRORS")
                print("====================\n")

                print(result.row_errors())

            if result.has_validation_errors():

                print("\n====================")
                print("VALIDATION ERRORS")
                print("====================\n")

                print(result.invalid_rows)

            # =========================================
            # SUCCESS RESPONSE
            # =========================================

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

            }, status=200)

        except Exception as e:

            import traceback

            print("\n====================")
            print("IMPORT ERROR")
            print("====================\n")

            traceback.print_exc()

            print("\nERROR:", repr(e))

            return Response({

                "success": False,

                "error": repr(e)

            }, status=500)


# =========================================
# EXPORT STUDENTS
# =========================================

class StudentExportAPIView(APIView):

    def get(self, request):

        print("\n====================")
        print("EXPORT API CALLED")
        print("====================\n")

        try:

            resource = StudentResource()

            dataset = resource.export()

            print("EXPORT SUCCESS")

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

        except Exception as e:

            import traceback

            print("\n====================")
            print("EXPORT ERROR")
            print("====================\n")

            traceback.print_exc()

            print("\nERROR:", repr(e))

            return Response({

                "success": False,

                "error": repr(e)

            }, status=500)