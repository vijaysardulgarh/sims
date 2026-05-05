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
# 🔹 STUDENT STRENGTH REPORT (FULL ORIGINAL LOGIC)
# =====================================================
class StudentStrengthReportAPIView(APIView):

    def get(self, request):

        school = get_current_school(request)
        if not school:
            return Response({"error": "School not selected"}, status=400)

        # ---------- CLASS MAPPING ----------
        class_mapping = {
            "sixth": "6th", "seventh": "7th", "eighth": "8th",
            "nineth": "9th", "ninth": "9th",
            "tenth": "10th", "eleventh": "11th", "twelfth": "12th",
        }

        class_order = {c: i for i, c in enumerate(class_mapping.keys())}
        category_list = ["SC", "BC-A", "BC-B", "GEN"]

        # ---------- DATA COLLECTION ----------
        section_data = defaultdict(lambda: [0] * 8)

        students = Student.objects.exclude(studentclass__isnull=True).exclude(section__isnull=True)

        for student in students:
            cls = (student.studentclass or "").strip().lower()
            sec = (student.section or "NA").strip().upper()
            gender = (student.gender or "").strip().lower()
            category = (student.category or "").strip().upper()

            if cls not in class_mapping:
                continue

            if category not in category_list:
                category = "GEN"

            base = category_list.index(category) * 2

            if gender == "female":
                section_data[(cls, sec)][base + 1] += 1
            else:
                section_data[(cls, sec)][base] += 1

        # ---------- TABLE BUILDER ----------
        def build_table_data(classes_subset):

            data = [
                ["Class", "Section",
                 "SC", "", "", "BCA", "", "", "BCB", "", "", "GEN", "", "", "OVERALL", "", ""],

                ["", "",
                 "M", "F", "T",
                 "M", "F", "T",
                 "M", "F", "T",
                 "M", "F", "T",
                 "M", "F", "T"],
            ]

            block_total = [0] * 8

            for cls in sorted(classes_subset, key=lambda c: class_order.get(c, 999)):
                class_total = [0] * 8

                for (cur_cls, sec), counts in sorted(section_data.items(), key=lambda x: x[0][1]):
                    if cur_cls != cls:
                        continue

                    sc = counts[0] + counts[1]
                    bca = counts[2] + counts[3]
                    bcb = counts[4] + counts[5]
                    gen = counts[6] + counts[7]

                    overall_m = counts[0] + counts[2] + counts[4] + counts[6]
                    overall_f = counts[1] + counts[3] + counts[5] + counts[7]
                    overall_t = overall_m + overall_f

                    data.append([
                        class_mapping.get(cur_cls, cur_cls), sec,
                        counts[0], counts[1], sc,
                        counts[2], counts[3], bca,
                        counts[4], counts[5], bcb,
                        counts[6], counts[7], gen,
                        overall_m, overall_f, overall_t
                    ])

                    class_total = [a + b for a, b in zip(class_total, counts)]

                # ---------- CLASS TOTAL ----------
                if sum(class_total) > 0:
                    sc = class_total[0] + class_total[1]
                    bca = class_total[2] + class_total[3]
                    bcb = class_total[4] + class_total[5]
                    gen = class_total[6] + class_total[7]

                    overall_m = class_total[0] + class_total[2] + class_total[4] + class_total[6]
                    overall_f = class_total[1] + class_total[3] + class_total[5] + class_total[7]
                    overall_t = overall_m + overall_f

                    data.append([
                        f"Total {class_mapping.get(cls, cls)}", "",
                        class_total[0], class_total[1], sc,
                        class_total[2], class_total[3], bca,
                        class_total[4], class_total[5], bcb,
                        class_total[6], class_total[7], gen,
                        overall_m, overall_f, overall_t
                    ])

                    block_total = [a + b for a, b in zip(block_total, class_total)]

            # ---------- BLOCK TOTAL ----------
            sc = block_total[0] + block_total[1]
            bca = block_total[2] + block_total[3]
            bcb = block_total[4] + block_total[5]
            gen = block_total[6] + block_total[7]

            overall_m = block_total[0] + block_total[2] + block_total[4] + block_total[6]
            overall_f = block_total[1] + block_total[3] + block_total[5] + block_total[7]
            overall_t = overall_m + overall_f

            data.append([
                "Block Total", "",
                block_total[0], block_total[1], sc,
                block_total[2], block_total[3], bca,
                block_total[4], block_total[5], bcb,
                block_total[6], block_total[7], gen,
                overall_m, overall_f, overall_t
            ])

            return data

        # ---------- PDF ----------
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="student_strength.pdf"'

        doc = SimpleDocTemplate(response, pagesize=landscape(A4), leftMargin=20, rightMargin=20)
        styles = getSampleStyleSheet()
        elements = []

        col_widths = [60, 60] + [35] * 15

        # ---------- STYLE ----------
        def style_table(table, data):

            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B3D91")),
                ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#4682B4")),
                ("TEXTCOLOR", (0, 0), (-1, 1), colors.white),

                ("FONTNAME", (0, 0), (-1, 1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),

                ("ALIGN", (2, 2), (-1, -1), "CENTER"),
                ("ALIGN", (0, 2), (1, -1), "LEFT"),

                ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),

                ("SPAN", (0, 0), (0, 1)),
                ("SPAN", (1, 0), (1, 1)),
                ("SPAN", (2, 0), (4, 0)),
                ("SPAN", (5, 0), (7, 0)),
                ("SPAN", (8, 0), (10, 0)),
                ("SPAN", (11, 0), (13, 0)),
                ("SPAN", (14, 0), (16, 0)),
            ]))

            # zebra rows
            for i in range(2, len(data)):
                if i % 2 == 0:
                    table.setStyle([("BACKGROUND", (0, i), (-1, i), colors.whitesmoke)])

            # totals
            for i, row in enumerate(data):
                if isinstance(row[0], str) and row[0].startswith("Total"):
                    table.setStyle([
                        ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#FFF2CC")),
                        ("FONTNAME", (0, i), (-1, i), "Helvetica-Bold"),
                        ("SPAN", (0, i), (1, i)),
                    ])

                if row[0] == "Block Total":
                    table.setStyle([
                        ("BACKGROUND", (0, i), (-1, i), colors.HexColor("#D9D9D9")),
                        ("FONTNAME", (0, i), (-1, i), "Helvetica-Bold"),
                        ("SPAN", (0, i), (1, i)),
                        ("LINEABOVE", (0, i), (-1, i), 1, colors.black),
                    ])

        # ---------- PAGE 1 ----------
        elements.append(Paragraph(
            "<para align='center'><font size=16><b>STUDENT STRENGTH REPORT (6th–8th)</b></font></para>",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 12))

        table1 = Table(build_table_data(["sixth", "seventh", "eighth"]), colWidths=col_widths, repeatRows=2)
        style_table(table1, table1._cellvalues)
        elements.append(table1)
        elements.append(PageBreak())

        # ---------- PAGE 2 ----------
        elements.append(Paragraph(
            "<para align='center'><font size=16><b>STUDENT STRENGTH REPORT (9th–12th)</b></font></para>",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 12))

        table2 = Table(build_table_data(["ninth", "nineth", "tenth", "eleventh", "twelfth"]), colWidths=col_widths, repeatRows=2)
        style_table(table2, table2._cellvalues)
        elements.append(table2)

        doc.build(elements)

        return response