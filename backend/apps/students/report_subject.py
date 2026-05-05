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
# 🔹 SUBJECT REPORT LINK API
# =====================================================
class SubjectReportLinkAPIView(APIView):

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
# 🔹 SUBJECT REPORT PDF (FULL ORIGINAL LOGIC)
# =====================================================
class SubjectReportPDFAPIView(APIView):

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
        response["Content-Disposition"] = f'attachment; filename="subject_report_{class_name}_{section_name}.pdf"'

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20,
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
        ]))

        elements.append(info_table)
        elements.append(Spacer(1, 12))

        # ---------- TABLE ----------
        data = [["SRN", "Roll No", "Student Name", "Subjects"]]

        for student in students:

            # ================= SUBJECT FILTER =================
            filtered_subjects = ""

            if student.subjects_opted:
                subject_list = str(student.subjects_opted).split(',')

                ordered = {
                    "Compulsory": [],
                    "Optional": [],
                    "Optional 1": [],
                    "Optional 2": [],
                    "NSQF": [],
                    "Language": [],
                    "Additional": []
                }

                for subject in subject_list:
                    parts = subject.split(':', 1)
                    if len(parts) == 2:
                        subject_type, subject_name = parts
                        subject_type = subject_type.strip()
                        subject_name = subject_name.strip()

                        if subject_type in ordered:
                            ordered[subject_type].append(subject_name)

                custom_order = [
                    "Physics", "Chemistry", "Geography",
                    "Fine Arts", "Political Science", "Physical Education"
                ]

                def custom_sort(subjects):
                    return sorted(
                        subjects,
                        key=lambda x: (
                            custom_order.index(x) if x in custom_order else len(custom_order),
                            x.lower()
                        )
                    )

                final_list = []

                for key in ["Compulsory", "Optional", "Optional 1", "Optional 2"]:
                    final_list.extend(custom_sort(ordered[key]))

                for key in ["NSQF", "Language"]:
                    final_list.extend(ordered[key])

                final_list.extend([f"Additional: {s}" for s in ordered["Additional"]])

                seen = set()
                final_list = [x for x in final_list if not (x in seen or seen.add(x))]

                filtered_subjects = ", ".join(final_list)

            # ================= NAME FORMAT =================
            student_name = (student.full_name_aadhar or "").title()
            father_name = (student.father_full_name_aadhar or "").title()
            mother_name = (student.mother_full_name_aadhar or "").title()

            relation = "C/o"
            if student.gender:
                g = student.gender.strip().lower()
                if g in ["male", "m"]:
                    relation = "S/o"
                elif g in ["female", "f"]:
                    relation = "D/o"

            if father_name and mother_name:
                name_with_parents = f"{student_name} {relation} {father_name} and {mother_name}"
            elif father_name:
                name_with_parents = f"{student_name} {relation} {father_name}"
            elif mother_name:
                name_with_parents = f"{student_name} and {mother_name}"
            else:
                name_with_parents = student_name

            data.append([
                student.srn,
                student.roll_number,
                name_with_parents,
                filtered_subjects
            ])

        table = Table(data, repeatRows=1, colWidths=[50, 30, 235, 355])

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#F9E79F")),
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 8),
            ("ALIGN", (0,0), (1,-1), "CENTER"),
            ("ALIGN", (2,0), (3,-1), "LEFT"),
        ]))

        elements.append(table)

        # ---------- SIGNATURE ----------
        elements.append(Spacer(1, 40))

        signature_table = Table(
            [
                ["_________________", "", "_________________"],
                ["Class Incharge", "", "Principal"]
            ],
            colWidths=[250, 100, 250]
        )

        signature_table.setStyle(TableStyle([
            ("ALIGN", (0,0), (0,-1), "LEFT"),
            ("ALIGN", (2,0), (2,-1), "RIGHT"),
            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 10),
            ("TOPPADDING", (0,0), (-1,-1), 20),
        ]))

        elements.append(signature_table)

        # ---------- PAGE NUMBER ----------
        def add_page_number(canvas, doc):
            canvas.saveState()
            canvas.setFont("Helvetica", 8)
            canvas.drawString(750, 15, f"Page {doc.page}")
            canvas.restoreState()

        doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)

        return response