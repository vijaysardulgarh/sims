from datetime import datetime

from rest_framework.views import APIView

from django.http import HttpResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    PageBreak,
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.enums import (
    TA_CENTER
)

from reportlab.lib.pagesizes import (
    A4
)

from .student_strength import (
    StudentStrengthAPIView
)


class StudentStrengthPDFAPIView(
    APIView
):

    def get(self, request):

        response = HttpResponse(
            content_type="application/pdf"
        )

        response[
            "Content-Disposition"
        ] = (
            'attachment; filename="student_strength.pdf"'
        )

        doc = SimpleDocTemplate(

            response,

            pagesize=A4,

            leftMargin=20,
            rightMargin=20,
            topMargin=20,
            bottomMargin=20,

        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        # =====================================
        # SCHOOL DETAILS
        # =====================================

        school_name = (
            "ABC PUBLIC SCHOOL"
        )

        school_address = (
            "New Delhi, Delhi - 110001"
        )

        school_phone = (
            "Phone: 9876543210"
        )

        generated_on = (
            datetime.now()
            .strftime(
                "%d-%b-%Y %I:%M %p"
            )
        )

        school_style = (
            styles["Title"]
        )

        school_style.alignment = (
            TA_CENTER
        )

        title_style = (
            styles["Heading1"]
        )

        title_style.alignment = (
            TA_CENTER
        )

        # =====================================
        # HEADER
        # =====================================

        elements.append(

            Paragraph(

                f"<b>{school_name}</b>",

                school_style

            )

        )

        elements.append(

            Paragraph(

                school_address,

                styles["Normal"]

            )

        )

        elements.append(

            Paragraph(

                school_phone,

                styles["Normal"]

            )

        )

        elements.append(
            Spacer(1, 15)
        )

        elements.append(

            Paragraph(

                "STUDENT STRENGTH REPORT",

                title_style

            )

        )

        elements.append(
            Spacer(1, 5)
        )

        elements.append(

            Paragraph(

                "Academic Session : 2025-26",

                styles["Normal"]

            )

        )

        elements.append(

            Paragraph(

                f"Generated On : {generated_on}",

                styles["Normal"]

            )

        )

        elements.append(
            Spacer(1, 12)
        )

        # =====================================
        # DATA
        # =====================================

        data = (
            StudentStrengthAPIView()
            .get(request)
            .data
        )

        junior_rows = []

        senior_rows = []

        for row in data:

            class_name = (
                row["class_name"]
                .replace(
                    "TOTAL ",
                    ""
                )
            )

            if class_name in [

                "6TH",
                "7TH",
                "8TH",

            ]:

                junior_rows.append(
                    row
                )

            else:

                senior_rows.append(
                    row
                )

        table_data = [

            [

                "Class",

                "Section",

                "SC",

                "BC-A",

                "BC-B",

                "GEN",

                "Total",

            ]

        ]

        class_total_rows = []

        grand_total_row = None

        grand_total = 0

        for row in data:

            class_label = (

                f"TOTAL {row['class_name']}"

                if row["row_type"] == "class_total"

                else (

                    "GRAND TOTAL"

                    if row["row_type"] == "grand_total"

                    else row["class_name"]

                )

            )

            section_label = (

                row["section_name"]

                if row["row_type"] == "section"

                else ""

            )

            table_data.append([

                class_label,

                section_label,

                row["sc_total"],

                row["bca_total"],

                row["bcb_total"],

                row["gen_total"],

                row["overall_total"],

            ])

            current_row = (
                len(table_data) - 1
            )

            if (
                row["row_type"]
                == "class_total"
            ):

                class_total_rows.append(
                    current_row
                )

            elif (
                row["row_type"]
                == "grand_total"
            ):

                grand_total_row = (
                    current_row
                )

                grand_total = (
                    row["overall_total"]
                )

        # =====================================
        # TABLE
        # =====================================

        table = Table(

            table_data,

            colWidths=[
                90,
                60,
                60,
                60,
                60,
                60,
                70,
            ]

        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#1F4E78"
                    )
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, 0),
                    11
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),

            ])

        )

        # =====================================
        # ZEBRA ROWS
        # =====================================

        for row_num in range(
            1,
            len(table_data)
        ):

            if row_num % 2 == 0:

                table.setStyle([

                    (

                        "BACKGROUND",

                        (0, row_num),

                        (-1, row_num),

                        colors.HexColor(
                            "#F7F9FC"
                        )

                    )

                ])

        # =====================================
        # CLASS TOTAL STYLING
        # =====================================

        for row_num in class_total_rows:

            table.setStyle([

                (

                    "BACKGROUND",

                    (0, row_num),

                    (-1, row_num),

                    colors.HexColor(
                        "#D9EAD3"
                    )

                ),

                (

                    "FONTNAME",

                    (0, row_num),

                    (-1, row_num),

                    "Helvetica-Bold"

                ),

            ])

        # =====================================
        # GRAND TOTAL STYLING
        # =====================================

        if grand_total_row:

            table.setStyle([

                (

                    "BACKGROUND",

                    (0, grand_total_row),

                    (-1, grand_total_row),

                    colors.HexColor(
                        "#FFF2CC"
                    )

                ),

                (

                    "FONTNAME",

                    (0, grand_total_row),

                    (-1, grand_total_row),

                    "Helvetica-Bold"

                ),

            ])

        elements.append(
            table
        )

        # =====================================
        # FOOTER
        # =====================================

        elements.append(
            Spacer(1, 15)
        )

        elements.append(

            Paragraph(

                f"<b>Total Students : {grand_total}</b>",

                styles["Normal"]

            )

        )

        elements.append(
            Spacer(1, 8)
        )

        elements.append(

            Paragraph(

                "Generated by SIMS ERP",

                styles["Italic"]

            )

        )

        # =====================================
        # BUILD PDF
        # =====================================

        doc.build(
            elements
        )

        return response