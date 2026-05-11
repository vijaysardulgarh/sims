from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from rest_framework import generics

from django.http import HttpResponse

from tablib import Dataset

from apps.students.student_resource import (
    StudentResource
)

from apps.students.models import (
    Student
)

from apps.students.serializers import (
    StudentSerializer
)


# =========================================
# STUDENT LIST CREATE API
# =========================================

class StudentListCreateAPIView(

    generics.ListCreateAPIView
):

    queryset = Student.objects.all().order_by(
        "-srn"
    )

    serializer_class = StudentSerializer


# =========================================
# STUDENT DETAIL API
# =========================================

class StudentRetrieveUpdateDestroyAPIView(

    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    lookup_field = "srn"

    # =====================================
    # PATCH UPDATE
    # =====================================

    def patch(self, request, *args, **kwargs):

        try:

            # =============================
            # GET STUDENT
            # =============================

            student = self.get_object()

            # =============================
            # UPDATE STATUS
            # =============================

            if "is_active" in request.data:

                student.is_active = request.data.get(
                    "is_active"
                )

                student.save()

                return Response({

                    "success": True,

                    "message":
                        "Status Updated Successfully",

                    "is_active":
                        student.is_active
                })

            # =============================
            # NO STATUS PROVIDED
            # =============================

            return Response({

                "success": False,

                "message":
                    "No status provided"

            }, status=400)

        except Exception as e:

            return Response({

                "success": False,

                "error": str(e)

            }, status=500)

    # =====================================
    # NORMAL UPDATE
    # =====================================

    def update(self, request, *args, **kwargs):

        partial = True

        instance = self.get_object()

        serializer = self.get_serializer(

            instance,

            data=request.data,

            partial=partial
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
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