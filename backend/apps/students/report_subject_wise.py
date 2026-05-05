from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from apps.core.utils import get_current_school
from apps.students.models import Student

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

import datetime


# =====================================================
# 🔹 SUBJECT-WISE LINK API (CLASSES + SUBJECTS)
# =====================================================
class SubjectWiseLinkAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        # -------- CLASSES --------
        classes = list(
            Student.objects.filter(school_name=school)
            .values_list("studentclass", flat=True)
            .distinct()
        )

        # -------- SUBJECTS --------
        subjects_set = set()

        students = Student.objects.filter(
            school_name=school
        ).exclude(subjects_opted__isnull=True)

        for s in students:
            for sub in str(s.subjects_opted).split(","):
                parts = sub.split(":", 1)
                if len(parts) == 2:
                    subjects_set.add(parts[1].strip())

        subjects = sorted(subjects_set)

        return Response({
            "classes": classes,
            "subjects": subjects
        })


# =====================================================
# 🔹 SUBJECT-WISE STUDENTS PDF
# =====================================================
class SubjectWiseStudentsPDFAPIView(APIView):

    def get(self, request, class_name, subject_name):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        # ---------- FILTER ----------
        students = Student.objects.filter(
            school_name=school.name,
            studentclass=class_name,
            subjects_opted__icontains=f":{subject_name}"
        ).order_by("section", "roll_number")

        # ---------- PDF ----------
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{subject_name}_{class_name}_students.pdf"'

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            rightMargin=20, leftMargin=20,
            topMargin=20, bottomMargin=20
        )

        elements = []
        styles = getSampleStyleSheet()

        # ---------- STYLES ----------
        title_style = ParagraphStyle(
            name="Title",
            alignment=1,
            fontSize=16,
            fontName="Helvetica-Bold"
        )

        sub_style = ParagraphStyle(
            name="SubTitle",
            alignment=1,
            fontSize=11
        )

        # ---------- HEADER ----------
        elements.append(Paragraph(f"{school.name}", title_style))
        elements.append(Spacer(1, 6))

        elements.append(Paragraph("<b>Subject Wise Students Report</b>", sub_style))

        elements.append(Paragraph(
            f"Class: {class_name}    Subject: {subject_name}    Date: {datetime.date.today().strftime('%d-%m-%Y')}",
            sub_style
        ))

        elements.append(Spacer(1, 12))

        # ---------- NAME FORMAT ----------
        def format_name(s):
            name = (s.full_name_aadhar or "").title()
            father = (s.father_full_name_aadhar or "").title()
            mother = (s.mother_full_name_aadhar or "").title()

            relation = "C/o"
            if s.gender:
                g = s.gender.lower()
                if g in ["male", "m"]:
                    relation = "S/o"
                elif g in ["female", "f"]:
                    relation = "D/o"

            if father and mother:
                return f"{name} {relation} {father} and {mother}"
            elif father:
                return f"{name} {relation} {father}"

            return name

        # ---------- TABLE ----------
        data = [["Sr. No.", "SRN", "Class", "Section", "Roll No", "Student Name"]]

        total_students = 0

        for i, s in enumerate(students, start=1):
            data.append([
                i,
                s.srn,
                class_name,
                s.section if s.section else "N/A",
                s.roll_number,
                format_name(s)
            ])
            total_students += 1

        table = Table(
            data,
            repeatRows=1,
            colWidths=[50, 70, 70, 70, 70, 300]
        )

        table.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),

            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0B3D91")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("BACKGROUND", (0,1), (-1,-1), colors.white),

            ("ALIGN", (0,0), (4,-1), "CENTER"),
            ("ALIGN", (5,1), (5,-1), "LEFT"),
        ]))

        elements.append(table)

        # ---------- TOTAL ----------
        elements.append(Spacer(1, 10))

        elements.append(Paragraph(
            f"<b>Total Students: {total_students}</b>",
            ParagraphStyle(name="Total", alignment=1, fontSize=11)
        ))

        # ---------- FOOTER ----------
        elements.append(Spacer(1, 25))

        footer = Table([
            ["__________________", "", "__________________"],
            ["Class Teacher", "", "Principal"]
        ], colWidths=[250, 100, 250])

        footer.setStyle(TableStyle([
            ("ALIGN", (0,0), (0,-1), "LEFT"),
            ("ALIGN", (2,0), (2,-1), "RIGHT"),
            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ]))

        elements.append(footer)

        # ---------- PAGE NUMBER ----------
        def add_page_number(canvas, doc):
            canvas.setFont("Helvetica", 8)
            canvas.drawString(750, 15, f"Page {doc.page}")

        doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)

        return response