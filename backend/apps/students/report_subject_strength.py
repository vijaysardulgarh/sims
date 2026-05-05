from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from collections import defaultdict

from apps.core.utils import get_current_school
from apps.students.models import Student

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


# =====================================================
# 🔹 SUBJECT STRENGTH REPORT (FULL ORIGINAL LOGIC)
# =====================================================
class SubjectStrengthReportAPIView(APIView):

    def get(self, request):

        # ---------- SCHOOL ----------
        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        # ---------- CLASS MAPPING ----------
        class_mapping = {
            "Sixth": "6th", "Seventh": "7th", "Eighth": "8th",
            "Nineth": "9th", "Ninth": "9th",
            "Tenth": "10th", "Eleventh": "11th", "Twelfth": "12th",
        }

        class_order = {c: i for i, c in enumerate(class_mapping.keys())}

        # ---------- SUBJECTS ----------
        subjects = [
            "Punjabi", "English", "Hindi", "Mathematics",
            "Science", "Social Science",
            "Physics", "Chemistry", "Biology",
            "Political Science", "Geography",
            "Economics", "Accountancy", "Business Studies",
            "Computer Science", "Physical Education",
            "Fine Arts", "Music", "Drawing",
            "Psychology", "Home Science",
            "Sanskrit",
            "IT-ITes",
            "Tourism & Hospitality"
        ]

        # ---------- SHORT NAMES ----------
        subject_short = {
            "Punjabi": "Pbi", "English": "Eng", "Hindi": "Hin",
            "Mathematics": "Math", "Science": "Sci", "Social Science": "S.St",
            "Physics": "Phy", "Chemistry": "Chem", "Biology": "Bio",
            "Political Science": "Pol.Sc", "Geography": "Geo",
            "Economics": "Eco", "Accountancy": "Acc", "Business Studies": "B.St",
            "Computer Science": "Comp", "Physical Education": "Phy.Ed",
            "Fine Arts": "F.Art", "Music": "Mus", "Drawing": "Draw",
            "Psychology": "Psy", "Home Science": "H.Sc",
            "Sanskrit": "San",
            "IT-ITes": "IT",
            "Tourism & Hospitality": "T&H"
        }

        # ---------- MATCH FUNCTION ----------
        def match_subject(opted, sub):
            o = (opted or "").lower()

            if sub == "IT-ITes":
                return "it" in o or "ites" in o

            if sub == "Tourism & Hospitality":
                return "tourism" in o or "hospitality" in o

            return sub.lower() in o

        # ---------- DATA ----------
        data_map = defaultdict(lambda: {sub: 0 for sub in subjects})

        students = Student.objects.filter(school_name=school.name)

        for s in students:
            cls = (s.studentclass or "").strip()
            sec = (s.section or "NA").strip().upper()
            opted = s.subjects_opted or ""

            if cls not in class_mapping:
                continue

            for sub in subjects:
                if match_subject(opted, sub):
                    data_map[(cls, sec)][sub] += 1

        # ---------- TABLE BUILDER ----------
        def build_table(classes_subset):

            header = ["Class", "Section"] + [subject_short.get(sub, sub) for sub in subjects]
            data = [header]

            block_total = {sub: 0 for sub in subjects}

            for cls in sorted(classes_subset, key=lambda c: class_order.get(c, 999)):
                class_total = {sub: 0 for sub in subjects}

                for (c, sec), sub_data in sorted(data_map.items(), key=lambda x: x[0][1]):
                    if c != cls:
                        continue

                    row = [class_mapping.get(c, c), sec]

                    for sub in subjects:
                        val = sub_data[sub]
                        row.append(val)
                        class_total[sub] += val

                    data.append(row)

                # ---------- CLASS TOTAL ----------
                if any(class_total.values()):
                    row = [f"Total {class_mapping.get(cls, cls)}", ""]
                    for sub in subjects:
                        row.append(class_total[sub])
                        block_total[sub] += class_total[sub]

                    data.append(row)

            # ---------- BLOCK TOTAL ----------
            row = ["Block Total", ""]
            for sub in subjects:
                row.append(block_total[sub])

            data.append(row)

            return data

        # ---------- PDF ----------
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="subject_strength.pdf"'

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            leftMargin=12,
            rightMargin=12
        )

        styles = getSampleStyleSheet()
        elements = []

        col_widths = [50, 45] + [24] * len(subjects)

        # ---------- TABLE STYLE ----------
        def style_table(table, data):
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B3D91")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
            ]))

            # zebra rows
            for i in range(1, len(data)):
                if i % 2 == 0:
                    table.setStyle([("BACKGROUND", (0, i), (-1, i), colors.whitesmoke)])

            # class total
            for i, row in enumerate(data):
                if isinstance(row[0], str) and row[0].startswith("Total"):
                    table.setStyle([
                        ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#FFE699")),
                        ("FONTNAME", (0, i), (-1, i), "Helvetica-Bold"),
                        ("SPAN", (0, i), (1, i)),
                    ])

            # block total
            for i, row in enumerate(data):
                if row[0] == "Block Total":
                    table.setStyle([
                        ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#A6A6A6")),
                        ("FONTNAME", (0, i), (-1, i), "Helvetica-Bold"),
                        ("SPAN", (0, i), (1, i)),
                    ])

        # ---------- PAGE 1 ----------
        elements.append(Paragraph(
            "<para align='center'><font size=14><b>SUBJECT STRENGTH REPORT (6th–8th)</b></font></para>",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 10))

        data1 = build_table(["Sixth", "Seventh", "Eighth"])
        table1 = Table(data1, colWidths=col_widths, repeatRows=1)
        style_table(table1, data1)
        elements.append(table1)

        elements.append(PageBreak())

        # ---------- PAGE 2 ----------
        elements.append(Paragraph(
            "<para align='center'><font size=14><b>SUBJECT STRENGTH REPORT (9th–12th)</b></font></para>",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 10))

        data2 = build_table(["Nineth", "Ninth", "Tenth", "Eleventh", "Twelfth"])
        table2 = Table(data2, colWidths=col_widths, repeatRows=1)
        style_table(table2, data2)
        elements.append(table2)

        doc.build(elements)

        return response