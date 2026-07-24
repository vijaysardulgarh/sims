from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import SubjectConstraint
from apps.timetables.subject_requirements.models import SubjectRequirement
from .serializers import SubjectConstraintSerializer, BulkSubjectConstraintSerializer

class SubjectConstraintViewSet(viewsets.ModelViewSet):
    queryset = SubjectConstraint.objects.all()
    serializer_class = SubjectConstraintSerializer

    @action(detail=False, methods=['get', 'post'], url_path='bulk_assign')
    def bulk_assign(self, request):
        if request.method == 'GET':
            school_class_id = request.query_params.get('school_class')
            stream_id = request.query_params.get('stream')

            if not school_class_id:
                return Response({"error": "school_class parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Find constraints where the linked subject requirement matches class/stream
            queryset = self.get_queryset().filter(subject_requirement__school_class_id=school_class_id)
            if stream_id:
                queryset = queryset.filter(subject_requirement__stream_id=stream_id)
            else:
                queryset = queryset.filter(subject_requirement__stream__isnull=True)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = BulkSubjectConstraintSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            constraints = serializer.validated_data['constraints']

            with transaction.atomic():
                for c_data in constraints:
                    subject_requirement_id = c_data.get('subject_requirement_id')
                    if not subject_requirement_id:
                        continue

                    # Update or create the constraint row for this specific requirement
                    SubjectConstraint.objects.update_or_create(
                        subject_requirement_id=subject_requirement_id,
                        defaults={
                            'priority': c_data.get('priority', 5),
                            'max_periods_per_day': c_data.get('max_periods_per_day', 1),
                            'allow_consecutive_periods': c_data.get('allow_consecutive_periods', False),
                            'required_consecutive_periods': c_data.get('required_consecutive_periods', 1),
                            'spread_across_week': c_data.get('spread_across_week', True),
                            'avoid_first_period': c_data.get('avoid_first_period', False),
                            'avoid_last_period': c_data.get('avoid_last_period', False),
                            'preferred_time_slot': c_data.get('preferred_time_slot', 'ANY'),
                            'remarks': c_data.get('remarks', '')
                        }
                    )

            return Response({"status": "Subject constraints saved successfully."}, status=status.HTTP_201_CREATED)