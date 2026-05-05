from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from apps.core.utils import get_current_school
from apps.students.models import Student

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle,
    Spacer, Image
)
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

import datetime


# =====================================================
# 🔹 ROLL CALL LINK API
# =====================================================
class RollCallLinkAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        class_sections = (
            Student.objects.filter(school_name=school)
            .values("studentclass", "section")
            .distinct()
        )

        class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
        order_map = {name: i for i, name in enumerate(class_order)}

        class_sections = sorted(
            class_sections,
            key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"] or "")
        )

        return Response({
            "school": school.name,
            "class_sections": class_sections
        })


# =====================================================
# 🔹 ROLL CALL PDF (FULL ORIGINAL LOGIC)
# =====================================================
class RollCallPDFAPIView(APIView):

    def get(self, request, class_name, section_name):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        school_name = school.name
        school_address = getattr(school, 'address', '')
        school_logo = getattr(school, 'logo', None)

        students = Student.objects.filter(
            school_name=school.name,
            studentclass=class_name,
            section=section_name
        ).order_by("roll_number")

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="roll_call_register_{class_name}_{section_name}.pdf"'

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            rightMargin=20,
            leftMargin=20,
            topMargin=20,
            bottomMargin=20,
        )

        elements = []
        styles = getSampleStyleSheet()

        # ---------- STYLES ----------
        school_style = ParagraphStyle(
            name="SchoolTitle",
            fontSize=18,
            alignment=1,
            spaceAfter=4,
            fontName="Helvetica-Bold"
        )

        normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

        # ---------- HEADER ----------
        header_data = []

        if school_logo:
            try:
                logo = Image(school_logo.path, width=50, height=50)
                header_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
            except:
                header_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])
        else:
            header_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

        header_table = Table(header_data, colWidths=[60, 600, 60])

        header_table.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ]))

        elements.append(header_table)

        if school_address:
            elements.append(Paragraph(school_address, normal_center))

        elements.append(Spacer(1, 12))

        # ---------- CLASS INFO ----------
        info_table = Table(
            [[
                f"Class: {class_name}",
                f"Section: {section_name}",
                f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"
            ]],
            colWidths=[200, 200, 200],
        )

        info_table.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 10),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("TOPPADDING", (0,0), (-1,-1), 6),
        ]))

        elements.append(info_table)
        elements.append(Spacer(1, 12))

        # ---------- TABLE ----------
        data = [[
            "SRN", "Roll No", "Adm No", "Student's Name",
            "DOB", "Gender", "Aadhaar No",
            "Father's Name", "Mother's Name", "Mobile No.", "Category"
        ]]

        for student in students:
            data.append([
                student.srn,
                student.roll_number,
                student.admission_number,
                student.full_name_aadhar,
                student.date_of_birth.strftime("%d-%m-%Y") if student.date_of_birth else "",
                student.gender,
                student.aadhaar_number,
                student.father_full_name_aadhar,
                student.mother_full_name_aadhar,
                student.father_mobile,
                student.category,
            ])

        table = Table(
            data,
            repeatRows=1,
            colWidths=[50, 30, 40, 100, 70, 50, 80, 100, 100, 80, 70]
        )

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.black),
            ("ALIGN", (0,0), (2,-1), "CENTER"),
            ("ALIGN", (4,0), (4,-1), "LEFT"),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 8),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("BOX", (0,0), (-1,-1), 1, colors.black),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ]))

        # Alternate rows
        for i in range(1, len(data)):
            if i % 2 == 0:
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)
                ]))

        elements.append(table)

        # ---------- PAGE NUMBER ----------
        def add_page_number(canvas, doc):
            canvas.saveState()
            canvas.setFont("Helvetica", 8)
            canvas.drawString(750, 15, f"Page {doc.page}")
            canvas.restoreState()

        doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)

        return response