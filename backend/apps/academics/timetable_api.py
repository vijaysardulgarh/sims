from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from collections import defaultdict
from django.db.models import Count

from apps.core.utils import get_current_school
from apps.staff.models import Staff, TeacherSubjectAssignment
from apps.academics.models import Subject, ClassSubject, Class, Section, Classroom
from apps.academics.models import Day, TimetableSlot, Timetable


# =========================================
# GENERATE TIMETABLE
# =========================================
class TimetableGenerateAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        classes = Class.objects.filter(school=school)
        subjects = Subject.objects.filter(school=school)
        teachers = Staff.objects.filter(school=school)
        time_slots = TimetableSlot.objects.filter(school=school)

        return Response({
            "classes": list(classes.values()),
            "subjects": list(subjects.values()),
            "teachers": list(teachers.values()),
            "time_slots": list(time_slots.values()),
        })


# =========================================
# TEACHER SUBJECT ASSIGNMENT
# =========================================
class TeacherAssignmentAPIView(APIView):

    def get(self, request):

        teachers = Staff.objects.filter(staff_role="Teaching")

        sections = Section.objects.all()
        subjects = ClassSubject.objects.all()

        assignments = TeacherSubjectAssignment.objects.all()

        return Response({
            "teachers": list(teachers.values()),
            "sections": list(sections.values()),
            "subjects": list(subjects.values()),
            "assignments": list(assignments.values())
        })


    def post(self, request):

        data = request.data

        TeacherSubjectAssignment.objects.filter(
            teacher_id=data["teacher"],
            section_id=data["section"]
        ).delete()

        for subject_id in data.get("subjects", []):
            TeacherSubjectAssignment.objects.create(
                teacher_id=data["teacher"],
                section_id=data["section"],
                class_subject_id=subject_id
            )

        return Response({"message": "Assignment saved"})


# =========================================
# SUBJECTS BY SECTION
# =========================================
class SubjectsBySectionAPIView(APIView):

    def get(self, request):

        section_id = request.GET.get("section_id")

        if not section_id:
            return Response({"subjects": []})

        section = get_object_or_404(Section, id=section_id)

        class_subjects = ClassSubject.objects.filter(
            subject_class=section.sec_class,
            stream=section.stream,
            sub_stream=section.sub_stream
        )

        subjects = [
            {"id": cs.id, "name": cs.subject.name}
            for cs in class_subjects
        ]

        return Response({"subjects": subjects})


# =========================================
# CREATE TIMETABLE ENTRY
# =========================================
class TimetableCreateAPIView(APIView):

    def post(self, request):

        data = request.data

        tsa = get_object_or_404(
            TeacherSubjectAssignment,
            id=data["assignment_id"]
        )

        slot = get_object_or_404(
            TimetableSlot,
            day_id=data["day"],
            period_number=data["period"]
        )

        entry = Timetable.objects.create(
            teacher_assignment=tsa,
            slot=slot,
            classroom_id=data.get("classroom"),
        )

        return Response({"id": entry.id})


# =========================================
# TIMETABLE LIST
# =========================================
class TimetableListAPIView(APIView):

    def get(self, request):

        timetables = Timetable.objects.select_related(
            "teacher_assignment__teacher",
            "teacher_assignment__class_subject__subject",
            "teacher_assignment__section",
            "slot"
        )

        data = defaultdict(list)

        for t in timetables:
            data[t.slot.day.name].append({
                "period": t.slot.period_number,
                "teacher": t.teacher_assignment.teacher.name,
                "subject": t.teacher_assignment.class_subject.subject.name,
                "section": t.teacher_assignment.section.name,
            })

        return Response(dict(data))


# =========================================
# DASHBOARD REPORT
# =========================================
class TimetableDashboardAPIView(APIView):

    def get(self, request):

        sections = Section.objects.all()
        teachers = Staff.objects.filter(staff_role="Teaching")

        return Response({
            "sections": list(sections.values()),
            "teachers": list(teachers.values())
        })


# =========================================
# SECTION REPORT
# =========================================
class SectionReportAPIView(APIView):

    def get(self, request, section_id):

        entries = Timetable.objects.filter(
            teacher_assignment__section_id=section_id
        )

        result = defaultdict(list)

        for e in entries:
            result[e.slot.day.name].append({
                "period": e.slot.period_number,
                "subject": e.teacher_assignment.class_subject.subject.name,
                "teacher": e.teacher_assignment.teacher.name,
            })

        return Response(dict(result))


# =========================================
# TEACHER REPORT
# =========================================
class TeacherReportAPIView(APIView):

    def get(self, request, teacher_id):

        entries = Timetable.objects.filter(
            teacher_assignment__teacher_id=teacher_id
        )

        result = defaultdict(list)

        for e in entries:
            result[e.slot.day.name].append({
                "period": e.slot.period_number,
                "subject": e.teacher_assignment.class_subject.subject.name,
                "section": e.teacher_assignment.section.name,
            })

        return Response(dict(result))


# =========================================
# WORKLOAD REPORT
# =========================================
class TeacherWorkloadAPIView(APIView):

    def get(self, request):

        data = (
            Timetable.objects.values(
                "teacher_assignment__teacher__name"
            )
            .annotate(total=Count("id"))
        )

        return Response(list(data))


# =========================================
# DRAG & DROP TIMETABLE
# =========================================
class TimetableDragAPIView(APIView):

    def get(self, request):

        sections = Section.objects.all()
        assignments = TeacherSubjectAssignment.objects.all()

        return Response({
            "sections": list(sections.values()),
            "assignments": list(assignments.values())
        })


# =========================================
# UPDATE ENTRY (DRAG)
# =========================================
class TimetableUpdateAPIView(APIView):

    def post(self, request):

        data = request.data

        tsa = get_object_or_404(
            TeacherSubjectAssignment,
            id=data["entry_id"]
        )

        slot = get_object_or_404(
            TimetableSlot,
            day_id=data["day"],
            period_number=data["period"]
        )

        Timetable.objects.update_or_create(
            teacher_assignment=tsa,
            slot=slot
        )

        return Response({"success": True})


# =========================================
# REMOVE ENTRY
# =========================================
class TimetableRemoveAPIView(APIView):

    def post(self, request):

        tsa = get_object_or_404(
            TeacherSubjectAssignment,
            id=request.data["entry_id"]
        )

        Timetable.objects.filter(teacher_assignment=tsa).delete()

        return Response({"success": True})