from rest_framework.views import APIView
from rest_framework.response import Response
from apps.schools.models import School


# =========================================
# LIST SCHOOLS (REPLACES sims_index GET)
# =========================================
class SchoolListAPIView(APIView):

    def get(self, request):

        schools = School.objects.all()

        data = [
            {
                "id": s.id,
                "name": s.name,
            }
            for s in schools
        ]

        return Response(data)


# =========================================
# SELECT SCHOOL (REPLACES POST in sims_index)
# =========================================
class SelectSchoolAPIView(APIView):

    def post(self, request):

        school_id = request.data.get("school_id")

        if not school_id:
            return Response({"error": "School ID required"}, status=400)

        request.session["school_id"] = int(school_id)

        return Response({
            "message": "School selected",
            "school_id": school_id
        })


# =========================================
# CLEAR SCHOOL (REPLACES ?clear=1)
# =========================================
class ClearSchoolAPIView(APIView):

    def post(self, request):

        request.session.pop("school_id", None)

        return Response({"message": "School cleared"})


# =========================================
# CURRENT SELECTED SCHOOL (REPLACES index view)
# =========================================
class CurrentSchoolAPIView(APIView):

    def get(self, request):

        school_id = request.session.get("school_id")

        if not school_id:
            return Response({"selected_school": None})

        school = School.objects.filter(id=school_id).first()

        if not school:
            return Response({"selected_school": None})

        return Response({
            "selected_school": {
                "id": school.id,
                "name": school.name
            }
        })