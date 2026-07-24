from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import SubjectRequirement
from .serializers import SubjectRequirementSerializer, BulkSubjectRequirementSerializer

class SubjectRequirementViewSet(viewsets.ModelViewSet):
    queryset = SubjectRequirement.objects.all()
    serializer_class = SubjectRequirementSerializer

    @action(detail=False, methods=['get', 'post'], url_path='bulk_assign')
    def bulk_assign(self, request):
        if request.method == 'GET':
            school_class_id = request.query_params.get('school_class')
            stream_id = request.query_params.get('stream')

            if not school_class_id:
                return Response({"error": "school_class parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.get_queryset().filter(school_class_id=school_class_id)
            if stream_id:
                queryset = queryset.filter(stream_id=stream_id)
            else:
                queryset = queryset.filter(stream__isnull=True)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = BulkSubjectRequirementSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            school_class_id = serializer.validated_data['school_class']
            stream_id = serializer.validated_data.get('stream')
            requirements = serializer.validated_data['requirements']

            with transaction.atomic():
                # Clear existing requirements for this specific class/stream pairing
                existing_reqs = SubjectRequirement.objects.filter(school_class_id=school_class_id)
                if stream_id:
                    existing_reqs = existing_reqs.filter(stream_id=stream_id)
                else:
                    existing_reqs = existing_reqs.filter(stream__isnull=True)
                
                existing_reqs.delete()

                # Build new instances including all extended properties
                new_instances = []
                for req in requirements:
                    new_instances.append(
                        SubjectRequirement(
                            school_class_id=school_class_id,
                            stream_id=stream_id,
                            subject_id=req['subject_id'],
                            sub_stream=req.get('sub_stream', ''),
                            theory_periods_per_week=req.get('theory_periods_per_week', 0),
                            lab_periods_per_week=req.get('lab_periods_per_week', 0),
                            is_compulsory=req.get('is_compulsory', True),
                            is_shared=req.get('is_shared', False),
                            priority=req.get('priority', 0),
                            teachers_required=req.get('teachers_required', 1),
                            remarks=req.get('remarks', '')
                        )
                    )
                
                SubjectRequirement.objects.bulk_create(new_instances)

            return Response({"status": "Requirements saved successfully."}, status=status.HTTP_201_CREATED)