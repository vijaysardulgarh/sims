from rest_framework import serializers
from .models import SubjectRequirement
from apps.academics.subjects.models import Subject

class SubjectRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectRequirement
        fields = [
            'id', 'school_class', 'stream', 'sub_stream', 'subject', 
            'theory_periods_per_week', 'lab_periods_per_week',
            'is_compulsory', 'is_shared', 'priority', 'teachers_required', 'remarks'
        ]

class BulkSubjectRequirementSerializer(serializers.Serializer):
    school_class = serializers.IntegerField(required=True)
    stream = serializers.IntegerField(required=False, allow_null=True)
    requirements = serializers.ListField(
        child=serializers.DictField(), # Expects full attribute dictionaries per subject
        allow_empty=True
    )