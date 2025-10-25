
from django.shortcuts import render, get_object_or_404, redirect
from ..models.staff import Staff,TeacherAttendance,ClassIncharge,SanctionedPost
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.db.models import Count,Sum,Q
from ..models.student import Student
from ..models.school import School

def teacher_attendance(request):
    # Parse date (default to today)
    date_str = request.POST.get("date") or request.GET.get("date")
    date = parse_date(date_str) if date_str else timezone.now().date()
    if date is None:  # fallback if parse_date fails
        date = timezone.now().date()

    if request.method == "POST":
        # Clear old records for the date
        TeacherAttendance.objects.filter(date=date).delete()

        # Save new attendance
        for teacher in Staff.objects.filter(staff_role="Teaching"):
            present = request.POST.get(f"present_{teacher.id}") == "on"
            TeacherAttendance.objects.create(
                teacher=teacher,
                date=date,
                present=present
            )
        return redirect("teacher_attendance")

    # Teachers list
    teachers = Staff.objects.filter(staff_role="Teaching").order_by("name")

    # Existing records for that date
    attendance_records = {
        rec.teacher_id: rec for rec in TeacherAttendance.objects.filter(date=date)
    }

    # Attach record to each teacher object
    for teacher in teachers:
        teacher.attendance_record = attendance_records.get(teacher.id)

    return render(request, "staff/teacher_attendance.html", {
        "teachers": teachers,
        "date": date,
    })


def teacher_attendance_update(request, pk):
    record = get_object_or_404(TeacherAttendance, pk=pk)
    if request.method == "POST":
        record.present = request.POST.get("present") == "on"
        record.save()
        return redirect("teacher_attendance")
    return render(request, "staff/teacher_attendance_update.html", {"record": record})


def teacher_attendance_delete(request, pk):
    record = get_object_or_404(TeacherAttendance, pk=pk)
    if request.method == "POST":
        record.delete()
        return redirect("teacher_attendance")
    return render(request, "staff/teacher_attendance_delete.html", {"record": record})



def staff_by_role(request, role):
    staff_list = Staff.objects.filter(staff_role=role).order_by("name")
    return render(request, "staff/staff_by_role.html", {"role": role, "staff_list": staff_list})







def class_incharge_report(request):
    # Step 1: Count students by (studentclass, section)
    student_counts = (
        Student.objects.values("studentclass", "section")
        .annotate(strength=Count("srn"))
    )
    strength_lookup = {
        (s["studentclass"], s["section"]): s["strength"]
        for s in student_counts
    }

    # Step 2: Fetch incharges with section + staff
    incharges = ClassIncharge.objects.filter(active=True).select_related(
        "section__sec_class", "section__stream", "section__medium", "staff"
    )

    report_data = []
    for incharge in incharges:
        sec = incharge.section
        staff = incharge.staff

        # Match with Student data
        key = (sec.sec_class.name, sec.name)
        student_strength = strength_lookup.get(key, 0)

        report_data.append({
            "class": sec.sec_class.name,
            "section": sec.name,
            "stream": sec.stream.name if sec.stream else "",
            "sub_stream": sec.sub_stream or "",
            "medium": sec.medium.name if sec.medium else "",
            "teacher_name": staff.name,
            "contact": staff.mobile_number or staff.email,
            "student_strength": student_strength,
        })

    return render(request, "reports/class_incharge_report.html", {"report_data": report_data})








def staff_summary(request):
    school = get_object_or_404(School, id=request.session.get("school_id"))

    # Allowed post types in required order
    allowed_post_types = ["Principal", "PGT", "TGT", "Clerk", "Lab Attendent", "Class IV"]

    # 1. Fetch sanctioned posts
    sanctioned = (
        SanctionedPost.objects.filter(school=school, post_type__name__in=allowed_post_types)
        .values("post_type__name", "subject__name")
        .annotate(
            sanctioned_posts=Sum("total_posts"),
        )
    )

    sanctioned_map = {
        (row["post_type__name"], row["subject__name"]): row["sanctioned_posts"]
        for row in sanctioned
    }

    # 2. Fetch working staff
    staff_summary = (
        Staff.objects.filter(school=school, post_type__name__in=allowed_post_types)
        .values("post_type__name", "subject__name")
        .annotate(
            regular_working=Count("id", filter=Q(employment_type="Regular")),
            guest_working=Count("id", filter=Q(employment_type="Guest")),
            hkrnl_working=Count("id", filter=Q(employment_type="HKRNL")),
            male_working=Count("id", filter=Q(gender="Male")),
            female_working=Count("id", filter=Q(gender="Female")),
        )
    )

    staff_map = {
        (row["post_type__name"], row["subject__name"]): row
        for row in staff_summary
    }

    # 3. Merge (loop only over sanctioned posts)
    merged = []
    for key, sanctioned_posts in sanctioned_map.items():
        post_type, subject = key
        staff_data = staff_map.get(key, {})

        row = {
            "post_type__name": post_type,
            "subject__name": subject,
            "sanctioned_posts": sanctioned_posts,
            "regular_working": staff_data.get("regular_working", 0),
            "guest_working": staff_data.get("guest_working", 0),
            "hkrnl_working": staff_data.get("hkrnl_working", 0),
            "male_working": staff_data.get("male_working", 0),
            "female_working": staff_data.get("female_working", 0),
        }

        row["vacant"] = sanctioned_posts - row["regular_working"]
        row["net_vacancy"] = (
            sanctioned_posts
            - row["regular_working"]
            - row["guest_working"]
            - row["hkrnl_working"]
        )

        merged.append(row)

    # 4. Sort according to required order
    post_order = {name: i for i, name in enumerate(allowed_post_types)}
    merged.sort(key=lambda x: post_order.get(x["post_type__name"], 999))

    return render(request, "reports/staff_summary.html", {"summary": merged, "school": school})



def admin_staff(request): 
    return render(request, "admin_staff.html")

def teaching_staff(request): 
    return render(request, "teaching_staff.html")

def non_teaching_staff(request): 
    return render(request, "non_teaching_staff.html")

def support_staff(request): 
    return render(request, "support_staff.html")

def prospectus(request): 
    return render(request, "prospectus.html")