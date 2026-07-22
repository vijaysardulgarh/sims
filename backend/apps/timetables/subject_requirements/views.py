# --- IMPORTS ---
from django.db import transaction
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Ensure these match your actual app structure
from .models import SubjectRequirement
from .serializers import SubjectRequirementSerializer
# ---------------

class SubjectRequirementListView(ListAPIView):
    serializer_class = SubjectRequirementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_fields = [
        "school_class", 
        "stream", 
        "sub_stream", 
        "subject", 
        "is_active"
    ]
    
    search_fields = [
        "school_class__name",
        "stream__name",
        "sub_stream",
        "subject__name",
    ]
    
    # 1. FIXED: Removed display_order references, using __name instead
    ordering_fields = [
        "school_class__name",
        "stream__name",
        "subject__name",
        "theory_periods_per_week",
        "lab_periods_per_week",
    ]

    def get_queryset(self):
        return SubjectRequirement.objects.filter(
            is_deleted=False,
        ).select_related(
            "school_class",
            "stream",
            "subject",
            "section",
        ).order_by(
            # 2. FIXED: Removed display_order references, using __name instead
            "school_class__name",
            "stream__name",
            "subject__name",
        )


class SubjectRequirementBulkSaveView(APIView):
    @transaction.atomic
    def post(self, request):
        rows = request.data

        if not isinstance(rows, list):
            return Response(
                {"detail": "Expected a list of records."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        ids = [row["id"] for row in rows if row.get("id")]
        existing = {
            obj.id: obj
            for obj in SubjectRequirement.objects.filter(id__in=ids, is_deleted=False)
        }

        serializers_to_save = []
        errors = []

        # Validate
        for index, row in enumerate(rows, start=1):
            instance = existing.get(row.get("id"))
            serializer = SubjectRequirementSerializer(
                instance=instance,
                data=row,
                partial=True,
            )

            if serializer.is_valid():
                validated = serializer.validated_data

                school_class = validated.get("school_class", getattr(instance, "school_class", None))
                section = validated.get("section", getattr(instance, "section", None))
                stream = validated.get("stream", getattr(instance, "stream", None))
                sub_stream = validated.get("sub_stream", getattr(instance, "sub_stream", ""))
                subject = validated.get("subject", getattr(instance, "subject", None))

                duplicate = SubjectRequirement.objects.filter(
                    school_class=school_class,
                    section=section,
                    stream=stream,
                    sub_stream=sub_stream,
                    subject=subject,
                    is_deleted=False,
                ).exclude(
                    id=getattr(instance, "id", None)
                ).exists()

                if duplicate:
                    errors.append(
                        {
                            "row": index,
                            "errors": {
                                "subject": [
                                    "Subject requirement already exists for this Class/Section/Stream combination."
                                ]
                            },
                        }
                    )
                else:
                    serializers_to_save.append(serializer)
            else:
                errors.append(
                    {
                        "row": index,
                        "errors": serializer.errors,
                    }
                )

        if errors:
            return Response(
                {
                    "detail": "Validation failed.",
                    "errors": errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Save
        saved = []
        for serializer in serializers_to_save:
            obj = serializer.save(updated_by=request.user)
            saved.append(obj)

        return Response(
            {
                "message": "Subject requirements saved successfully.",
                "count": len(saved),
                "results": SubjectRequirementSerializer(saved, many=True).data,
            },
            status=status.HTTP_200_OK,
        )