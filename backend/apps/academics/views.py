from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q, Case, When

from apps.core.utils import get_current_school
from apps.students.models import Student
from apps.academics.models import ClassSubject


# =========================================
# SUBJECT STRENGTH (FULL ORIGINAL LOGIC)
# =========================================
class SubjectStrengthAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        class_order = {
            "Sixth": 1, "Seventh": 2, "Eighth": 3, "Nineth": 4,
            "Tenth": 5, "Eleventh": 6, "Twelfth": 7,
        }

        data = list(
            Student.objects.filter(school_name=school.name)
            .values("studentclass", "section", "stream")
            .annotate(
                punjabi=Count("srn", filter=Q(subjects_opted__icontains="Punjabi")),
                music=Count("srn", filter=Q(subjects_opted__icontains="Music")),
                accountancy=Count("srn", filter=Q(subjects_opted__icontains="Accountancy")),
                business_studies=Count("srn", filter=Q(subjects_opted__icontains="Business Studies")),
                economics=Count("srn", filter=Q(subjects_opted__icontains="Economics")),
                sanskrit=Count("srn", filter=Q(subjects_opted__icontains="Sanskrit")),
                fine_arts=Count("srn", filter=Q(subjects_opted__icontains="Fine Arts")),
                political_science=Count("srn", filter=Q(subjects_opted__icontains="Political Science")),
                geography=Count("srn", filter=Q(subjects_opted__icontains="Geography")),
                mathematics=Count("srn", filter=Q(subjects_opted__icontains="Mathematics")),
                psychology=Count("srn", filter=Q(subjects_opted__icontains="Psychology")),
                drawing=Count("srn", filter=Q(subjects_opted__icontains="Drawing")),
                english=Count("srn", filter=Q(subjects_opted__icontains="English")),
                hindi=Count("srn", filter=Q(subjects_opted__icontains="Hindi")),
                social_science=Count("srn", filter=Q(subjects_opted__icontains="Social Science")),

                science=Count("srn", filter=Q(subjects_opted__iregex=r"\bScience(\s*(and|&)\s*Technology)?\b")),

                physics=Count("srn", filter=Q(subjects_opted__icontains="Physics")),
                chemistry=Count("srn", filter=Q(subjects_opted__icontains="Chemistry")),
                biology=Count("srn", filter=Q(subjects_opted__icontains="Biology")),
                home_science=Count("srn", filter=Q(subjects_opted__icontains="Home Science")),

                physical_education=Count("srn", filter=Q(subjects_opted__icontains="Physical and Health Education") | Q(subjects_opted__icontains="Physical Education")),
                automobile=Count("srn", filter=Q(subjects_opted__icontains="Automotive")),
                beauty_wellness=Count("srn", filter=Q(subjects_opted__icontains="Beauty & Wellness")),
                computer_science=Count("srn", filter=Q(subjects_opted__icontains="Computer Science")),

                order=Case(*[When(studentclass=cls, then=pos) for cls, pos in class_order.items()])
            )
            .order_by("order")
        )

        return Response(data)


# =========================================
# SUBJECTS OFFERED (FULL ORIGINAL LOGIC)
# =========================================
class SubjectsOfferedAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        class_subjects = (
            ClassSubject.objects
            .select_related("subject_class", "stream", "subject")
            .filter(subject_class__school=school)
            .order_by("subject_class__name", "subject__name")
        )

        def get_level(class_name):
            try:
                num = int("".join([c for c in class_name if c.isdigit()]))
            except:
                return "Other"

            if 1 <= num <= 5:
                return "Primary"
            elif 6 <= num <= 8:
                return "Middle"
            elif 9 <= num <= 10:
                return "Secondary"
            elif 11 <= num <= 12:
                return "Senior Secondary"
            return "Other"

        grouped_data = {
            "Primary": {},
            "Middle": {},
            "Secondary": {},
            "Senior Secondary": {},
            "Other": {}
        }

        for cs in class_subjects:
            level = get_level(cs.subject_class.name)

            parts = [cs.subject_class.name]
            if cs.stream:
                parts.append(cs.stream.name)
            if cs.sub_stream:
                parts.append(cs.sub_stream)

            class_label = " - ".join(parts)

            grouped_data.setdefault(level, {})
            grouped_data[level].setdefault(class_label, [])

            grouped_data[level][class_label].append({
                "name": cs.subject.name,
                "periods_per_week": cs.periods_per_week,
                "is_optional": cs.is_optional,
                "has_lab": cs.has_lab,
            })

        return Response(grouped_data)