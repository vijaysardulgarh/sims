from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from apps.core.utils import get_current_school
from apps.students.models import Student

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


# =====================================================
# 🔹 BPL STUDENTS REPORT (FULL ORIGINAL LOGIC)
# =====================================================
class BPLStudentsReportAPIView(APIView):

    def get(self, request):

        # ---------- SCHOOL ----------
        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        # ---------- CLASS ORDER ----------
        CLASS_ORDER = {
            "Sixth": 6,
            "Seventh": 7,
            "Eighth": 8,
            "Nineth": 9,
            "Tenth": 10,
            "Eleventh": 11,
            "Twelfth": 12,
        }

        # ---------- FILTER STUDENTS ----------
        students = list(
            Student.objects.filter(
                school_name=school.name
            )
            .exclude(below_poverty_line_certificate_number__isnull=True)
            .exclude(below_poverty_line_certificate_number__exact="")
        )

        # ---------- SORT ----------
        students.sort(
            key=lambda s: (
                CLASS_ORDER.get(s.studentclass, 99),
                s.section or "",
                s.roll_number or 0
            )
        )

        # ---------- PDF RESPONSE ----------
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="bpl_students_{school.name}.pdf"'

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            rightMargin=20,
            leftMargin=20,
            topMargin=20,
            bottomMargin=20
        )

        elements = []
        styles = getSampleStyleSheet()

        # ---------- TITLE ----------
        title_style = ParagraphStyle(
            name="Title",
            fontSize=16,
            alignment=1,
            spaceAfter=10,
            fontName="Helvetica-Bold"
        )

        elements.append(Paragraph(f"BPL Students Report - {school.name}", title_style))
        elements.append(Spacer(1, 12))

        # ---------- TABLE HEADER ----------
        data = [[
            "SRN", "Class", "Section", "Roll No", "Student's Name",
            "DOB", "Gender", "Account No.", "Family ID",
            "BPL Certificate No.", "Category",
        ]]

        # ---------- TABLE ROWS ----------
        for s in students:
            data.append([
                s.srn,
                s.studentclass,
                s.section,
                s.roll_number,
                s.full_name_aadhar,
                s.date_of_birth.strftime("%d-%m-%Y") if s.date_of_birth else "",
                s.gender,
                s.account_number,
                s.family_id,
                s.below_poverty_line_certificate_number,
                s.category,
            ])

        # ---------- TABLE ----------
        table = Table(
            data,
            repeatRows=1,
            colWidths=[60, 50, 50, 40, 100, 70, 50, 90, 60, 80, 50]
        )

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("FONTSIZE", (0,0), (-1,-1), 8),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ]))

        elements.append(table)

        # ---------- BUILD PDF ----------
        doc.build(elements)

        return response