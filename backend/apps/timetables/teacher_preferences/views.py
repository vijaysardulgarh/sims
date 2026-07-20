from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.staff.profiles.models import Staff

from .models import TeacherPreference
from .serializers import TeacherPreferenceSerializer


class TeacherPreferenceListView(APIView):

    def get(self, request):

        teachers = Staff.objects.filter(
            is_deleted=False,
        ).order_by("name")

        data = []

        for teacher in teachers:

            preference, _ = TeacherPreference.objects.get_or_create(
                teacher=teacher,
                defaults={
                    "created_by": request.user,
                },
            )

            data.append(
                TeacherPreferenceSerializer(preference).data
            )

        return Response(data)


class TeacherPreferenceBulkSaveView(APIView):

    @transaction.atomic
    def post(self, request):

        serializer = TeacherPreferenceSerializer(
            data=request.data,
            many=True,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        for item in serializer.validated_data:

            teacher = item.pop("teacher")

            TeacherPreference.objects.update_or_create(
                teacher=teacher,
                defaults={
                    **item,
                    "updated_by": request.user,
                },
            )

        return Response(
            {
                "detail": "Teacher preferences saved successfully."
            },
            status=status.HTTP_200_OK,
        )