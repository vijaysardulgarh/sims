from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.db.models import Count, Sum, Q

from apps.staff.models import Staff, TeacherAttendance, ClassIncharge, SanctionedPost
from apps.students.models import Student
from apps.schools.models import School


# =========================================
# TEACHER ATTENDANCE (GET + POST)
# =========================================
class TeacherAttendanceAPIView(APIView):

    def get(self, request):

        date_str = request.GET.get("date")
        date = parse_date(date_str) if date_str else timezone.now().date()

        teachers = Staff.objects.filter(staff_role="Teaching").order_by("name")

        attendance_records = {
            rec.teacher_id: rec for rec in TeacherAttendance.objects.filter(date=date)
        }

        data = []

        for teacher in teachers:
            record = attendance_records.get(teacher.id)

            data.append({
                "teacher_id": teacher.id,
                "name": teacher.name,
                "present": record.present if record else False
            })

        return Response({
            "date": date,
            "teachers": data
        })


    def post(self, request):

        date_str = request.data.get("date")
        date = parse_date(date_str) if date_str else timezone.now().date()

        TeacherAttendance.objects.filter(date=date).delete()

        teachers = Staff.objects.filter(staff_role="Teaching")

        for teacher in teachers:
            present = request.data.get(f"present_{teacher.id}", False)

            TeacherAttendance.objects.create(
                teacher=teacher,
                date=date,
                present=bool(present)
            )

        return Response({"message": "Attendance saved"})


# =========================================
# UPDATE ATTENDANCE
# =========================================
class TeacherAttendanceUpdateAPIView(APIView):

    def put(self, request, pk):

        record = get_object_or_404(TeacherAttendance, pk=pk)

        record.present = request.data.get("present", False)
        record.save()

        return Response({"message": "Updated"})


# =========================================
# DELETE ATTENDANCE
# =========================================
class TeacherAttendanceDeleteAPIView(APIView):

    def delete(self, request, pk):

        record = get_object_or_404(TeacherAttendance, pk=pk)
        record.delete()

        return Response({"message": "Deleted"})


# =========================================
# STAFF BY ROLE
# =========================================
class StaffByRoleAPIView(APIView):

    def get(self, request, role):

        staff_list = Staff.objects.filter(staff_role=role).order_by("name")

        data = list(staff_list.values())

        return Response({
            "role": role,
            "staff": data
        })


# =========================================
# CLASS INCHARGE REPORT
# =========================================
class ClassInchargeReportAPIView(APIView):

    def get(self, request):

        student_counts = (
            Student.objects.values("studentclass", "section")
            .annotate(strength=Count("srn"))
        )

        strength_lookup = {
            (s["studentclass"], s["section"]): s["strength"]
            for s in student_counts
        }

        incharges = ClassIncharge.objects.filter(active=True).select_related(
            "section__sec_class", "section__stream", "section__medium", "staff"
        )

        data = []

        for incharge in incharges:
            sec = incharge.section
            staff = incharge.staff

            key = (sec.sec_class.name, sec.name)
            strength = strength_lookup.get(key, 0)

            data.append({
                "class": sec.sec_class.name,
                "section": sec.name,
                "stream": sec.stream.name if sec.stream else "",
                "sub_stream": sec.sub_stream or "",
                "medium": sec.medium.name if sec.medium else "",
                "teacher": staff.name,
                "contact": staff.mobile_number or staff.email,
                "student_strength": strength,
            })

        return Response(data)


# =========================================
# STAFF SUMMARY
# =========================================
class StaffSummaryAPIView(APIView):

    def get(self, request):

        school_id = request.session.get("school_id")
        school = get_object_or_404(School, id=school_id)

        allowed = ["Principal", "PGT", "TGT", "Clerk", "Lab Attendent", "Class IV"]

        sanctioned = (
            SanctionedPost.objects.filter(school=school, post_type__name__in=allowed)
            .values("post_type__name", "subject__name")
            .annotate(sanctioned_posts=Sum("total_posts"))
        )

        sanctioned_map = {
            (r["post_type__name"], r["subject__name"]): r["sanctioned_posts"]
            for r in sanctioned
        }

        staff_data = (
            Staff.objects.filter(school=school, post_type__name__in=allowed)
            .values("post_type__name", "subject__name")
            .annotate(
                regular=Count("id", filter=Q(employment_type="Regular")),
                guest=Count("id", filter=Q(employment_type="Guest")),
                hkrnl=Count("id", filter=Q(employment_type="HKRNL")),
                male=Count("id", filter=Q(gender="Male")),
                female=Count("id", filter=Q(gender="Female")),
            )
        )

        staff_map = {
            (r["post_type__name"], r["subject__name"]): r
            for r in staff_data
        }

        result = []

        for key, sanctioned_posts in sanctioned_map.items():
            post, subject = key
            s = staff_map.get(key, {})

            row = {
                "post": post,
                "subject": subject,
                "sanctioned": sanctioned_posts,
                "regular": s.get("regular", 0),
                "guest": s.get("guest", 0),
                "hkrnl": s.get("hkrnl", 0),
                "male": s.get("male", 0),
                "female": s.get("female", 0),
            }

            row["vacant"] = sanctioned_posts - row["regular"]
            row["net_vacancy"] = (
                sanctioned_posts - row["regular"] - row["guest"] - row["hkrnl"]
            )

            result.append(row)

        return Response(result)


# =========================================
# STATIC STAFF PAGES
# =========================================
class StaffStaticAPIView(APIView):

    def get(self, request):

        return Response({
            "admin_staff": True,
            "teaching_staff": True,
            "non_teaching_staff": True,
            "support_staff": True,
            "prospectus": True
        })