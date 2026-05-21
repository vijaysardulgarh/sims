from rest_framework.views import APIView
from rest_framework.response import Response

from apps.staff.profiles.models import Staff


class StaffByRoleAPIView(APIView):

    def get(self, request, role):

        staff_list = Staff.objects.filter(
            staff_role=role
        ).order_by("name")

        data = list(
            staff_list.values()
        )

        return Response({
            "role": role,
            "staff": data
        })


class StaffStaticAPIView(APIView):

    def get(self, request):

        return Response({
            "admin_staff": True,
            "teaching_staff": True,
            "non_teaching_staff": True,
            "support_staff": True,
            "prospectus": True
        })