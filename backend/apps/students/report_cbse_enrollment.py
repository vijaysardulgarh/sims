from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

import csv

from apps.students.models import Student
from apps.students.enrollment_subjects_utils import (
    get_student_cbse_subjects,
    get_medium_from_section
)

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


# =====================================================
# 🔹 CBSE ENROLLMENT PDF
# =====================================================
class CBSEEnrollmentPDFAPIView(APIView):

    def get(self, request):

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="cbse_enrollment.pdf"'

        # ---------- FONT ----------
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            leftMargin=10,
            rightMargin=10,
            topMargin=15,
            bottomMargin=15
        )

        elements = []
        styles = getSampleStyleSheet()

        normal_style = ParagraphStyle(
            "normal",
            fontSize=6,
            leading=7,
            alignment=1
        )

        # ---------- HEADERS ----------
        headers = [
            "CLASS","SECTION","ROLL_NO","CAT","CNAME","MNAME","FNAME",
            "SEX","CAST","HANDICAP",
            "SUB1","SUB2","SUB3","SUB4","SUB5","SUB6","SUB7",
            "D_O_B","ANNUAL_INC","ONLY_CHILD","ADM_SRL","ADM_DATE","MINORITY"
        ]

        data = [[Paragraph(h, normal_style) for h in headers]]

        # ---------- FILTER ----------
        minority_religions = {"MUSLIM", "CHRISTIAN", "SIKH", "BUDDHIST", "JAIN", "PARSI"}

        students = Student.objects.filter(
            studentclass__in=["Ninth", "Eleventh"]
        ).order_by("studentclass", "section", "roll_number")

        # ---------- ROWS ----------
        for s in students.iterator():

            slots = get_student_cbse_subjects(s, mark_invalid=True)

            minority_flag = "Y" if getattr(s, "religion", "").upper() in minority_religions else "N"

            row = [
                s.studentclass or "", s.section or "", s.roll_number or "", s.category or "",
                s.full_name_aadhar or "", s.mother_full_name_aadhar or "", s.father_full_name_aadhar or "",
                s.gender or "", s.caste or "", "Y" if s.disability else "N",

                slots.get("sub1", ""), slots.get("sub2", ""), slots.get("sub3", ""),
                slots.get("sub4", ""), slots.get("sub5", ""), slots.get("sub6", ""), slots.get("sub7", ""),

                s.date_of_birth.strftime("%d-%m-%Y") if s.date_of_birth else "",
                str(s.family_annual_income) if s.family_annual_income else "",
                "Y" if getattr(s, "only_child", False) else "N",
                s.admission_number or "",
                s.admission_date.strftime("%d-%m-%Y") if s.admission_date else "",
                minority_flag
            ]

            data.append([
                Paragraph(str(c) if c else " ", normal_style)
                for c in row
            ])

        # ---------- TABLE ----------
        col_widths = [30]*10 + [50]*7 + [35]*6

        table = Table(data, repeatRows=1, colWidths=col_widths)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("FONTSIZE", (0,0), (-1,-1), 6),
            ("GRID", (0,0), (-1,-1), 0.25, colors.grey),
        ]))

        elements.append(Paragraph("CBSE Enrollment Report", styles["Title"]))
        elements.append(table)

        doc.build(elements)

        return response


# =====================================================
# 🔹 CBSE ENROLLMENT CSV
# =====================================================
class CBSEEnrollmentCSVAPIView(APIView):

    def get(self, request):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cbse_enrollment.csv"'

        writer = csv.writer(response)

        headers = [
            "CLASS","SECTION","ROLL_NO","CAT","CNAME","MNAME","FNAME",
            "SEX","CAST","HANDICAP",
            "SUB1","MED1","SUB2","MED2","SUB3","MED3",
            "SUB4","MED4","SUB5","MED5","SUB6","MED6","SUB7","MED7",
            "D_O_B","ANNUAL_INC","ONLY_CHILD","ADM_SRL","ADM_DATE","MINORITY"
        ]

        writer.writerow(headers)

        minority_religions = {"MUSLIM", "CHRISTIAN", "SIKH", "BUDDHIST", "JAIN", "PARSI"}

        students = Student.objects.filter(
            studentclass__in=["Ninth", "Eleventh"]
        ).order_by("studentclass", "section", "roll_number")

        for s in students:

            slots = get_student_cbse_subjects(s, mark_invalid=True)
            medium = get_medium_from_section(getattr(s, "section", ""))

            minority_flag = "Y" if getattr(s, "religion", "").upper() in minority_religions else "N"

            writer.writerow([
                s.studentclass or "", s.section or "", s.roll_number or "", s.category or "",
                s.full_name_aadhar or "", s.mother_full_name_aadhar or "", s.father_full_name_aadhar or "",
                s.gender or "", s.caste or "", "Y" if s.disability else "N",

                slots.get("sub1",""), medium,
                slots.get("sub2",""), medium,
                slots.get("sub3",""), medium,
                slots.get("sub4",""), medium,
                slots.get("sub5",""), medium,
                slots.get("sub6",""), medium,
                slots.get("sub7",""), medium,

                s.date_of_birth.strftime("%d-%m-%Y") if s.date_of_birth else "",
                str(s.family_annual_income) if s.family_annual_income else "",
                "Y" if getattr(s, "only_child", False) else "N",
                s.admission_number or "",
                s.admission_date.strftime("%d-%m-%Y") if s.admission_date else "",
                minority_flag
            ])

        return response