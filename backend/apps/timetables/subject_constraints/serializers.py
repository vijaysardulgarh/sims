from rest_framework import serializers
from .models import SubjectConstraint
from apps.timetables.subject_requirements.serializers import SubjectRequirementSerializer

class SubjectConstraintSerializer(serializers.ModelSerializer):
    subject_requirement_detail = SubjectRequirementSerializer(source='subject_requirement', read_only=True)
    subject_name = serializers.CharField(source='subject_requirement.subject.name', read_only=True)

    class Meta:
        model = SubjectConstraint
        fields = [
            'id', 'subject_requirement', 'subject_requirement_detail', 'subject_name',
            'priority', 'max_periods_per_day', 'allow_consecutive_periods',
            'required_consecutive_periods', 'spread_across_week',
            'avoid_first_period', 'avoid_last_period', 'preferred_time_slot', 'remarks'
        ]

class BulkSubjectConstraintSerializer(serializers.Serializer):
    school_class = serializers.IntegerField(required=True)
    stream = serializers.IntegerField(required=False, allow_null=True)
    constraints = serializers.ListField(
        child=serializers.DictField(),
        allow_empty=True
    )