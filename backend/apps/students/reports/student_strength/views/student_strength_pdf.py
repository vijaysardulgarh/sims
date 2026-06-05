from rest_framework.views import APIView
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_CENTER

from .student_strength import StudentStrengthAPIView


class StudentStrengthPDFAPIView(APIView):
    def get(self, request):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="student_strength.pdf"'

        doc = SimpleDocTemplate(
            response,
            pagesize=landscape(A4),
            leftMargin=20,
            rightMargin=20,
            topMargin=30,
            bottomMargin=30,
        )

        styles = getSampleStyleSheet()
        
        # Create centered styles for the professional header
        centered_title = ParagraphStyle(
            name="CenteredTitle", 
            parent=styles["Title"], 
            alignment=TA_CENTER, 
            textColor=colors.HexColor("#1a365d")
        )
        centered_normal = ParagraphStyle(
            name="CenteredNormal", 
            parent=styles["Normal"], 
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4a5568")
        )
        centered_heading = ParagraphStyle(
            name="CenteredHeading", 
            parent=styles["Heading2"], 
            alignment=TA_CENTER,
            textColor=colors.HexColor("#2b6cb0")
        )

        # Fetch Data
        data = StudentStrengthAPIView().get(request).data

        # Define Table Headers
        table_data = [
            [
                "Class", "Section",
                "SC", "", "",
                "BC-A", "", "",
                "BC-B", "", "",
                "GEN", "", "",
                "OVERALL", "", ""
            ],
            [
                "", "",
                "M", "F", "T",
                "M", "F", "T",
                "M", "F", "T",
                "M", "F", "T",
                "M", "F", "T",
            ]
        ]

        class_total_rows = []
        grand_total_row = None

        # Populate Rows
        for row in data:
            if row["row_type"] == "class_total":
                class_name = f"TOTAL {row['class_name']}"
            elif row["row_type"] == "grand_total":
                class_name = "GRAND TOTAL"
            else:
                class_name = row["class_name"]

            table_data.append([
                class_name, row["section_name"],
                row["sc_male"], row["sc_female"], row["sc_total"],
                row["bca_male"], row["bca_female"], row["bca_total"],
                row["bcb_male"], row["bcb_female"], row["bcb_total"],
                row["gen_male"], row["gen_female"], row["gen_total"],
                row["overall_male"], row["overall_female"], row["overall_total"],
            ])

            current_row = len(table_data) - 1

            # Track total rows for styling later
            if row["row_type"] == "class_total":
                class_total_rows.append(current_row)
            elif row["row_type"] == "grand_total":
                grand_total_row = current_row

        # Configure Table Columns
        table = Table(
            table_data,
            colWidths=[80, 50, 30, 30, 35, 30, 30, 35, 30, 30, 35, 35, 35, 40, 40, 40, 45],
            repeatRows=2,
        )

        # ---------------------------------------------------------
        # THE FIX: Consolidate all styles into one massive list
        # ---------------------------------------------------------
        style_commands = [
            # Spanning headers
            ("SPAN", (0, 0), (0, 1)),
            ("SPAN", (1, 0), (1, 1)),
            ("SPAN", (2, 0), (4, 0)),
            ("SPAN", (5, 0), (7, 0)),
            ("SPAN", (8, 0), (10, 0)),
            ("SPAN", (11, 0), (13, 0)),
            ("SPAN", (14, 0), (16, 0)),

            # Header colors and fonts
            ("BACKGROUND", (0, 0), (-1, 1), colors.HexColor("#2b6cb0")),
            ("TEXTCOLOR", (0, 0), (-1, 1), colors.white),
            ("FONTNAME", (0, 0), (-1, 1), "Helvetica-Bold"),
            
            # Alignment
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            
            # Padding for readability
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]

        # Apply Class Total Backgrounds dynamically
        for row_num in class_total_rows:
            style_commands.extend([
                ("BACKGROUND", (0, row_num), (-1, row_num), colors.HexColor("#edf2f7")),
                ("FONTNAME", (0, row_num), (-1, row_num), "Helvetica-Bold"),
                ("TEXTCOLOR", (0, row_num), (-1, row_num), colors.black),
            ])

        # Apply Grand Total Backgrounds
        if grand_total_row:
            style_commands.extend([
                ("BACKGROUND", (0, grand_total_row), (-1, grand_total_row), colors.HexColor("#feebc8")),
                ("FONTNAME", (0, grand_total_row), (-1, grand_total_row), "Helvetica-Bold"),
                ("TEXTCOLOR", (0, grand_total_row), (-1, grand_total_row), colors.HexColor("#7b341e")),
            ])

        # IMPORTANT: Apply GRID and BOX at the very end so it sits on top of all backgrounds
        style_commands.append(("GRID", (0, 0), (-1, -1), 1, colors.black))
        
        # Set the fully compiled style to the table
        table.setStyle(TableStyle(style_commands))

        # Assemble the Document
        elements = [
            Paragraph("ABC PUBLIC SCHOOL", centered_title),
            Paragraph("New Delhi, Delhi - 110001 | Phone : +91 9876543210", centered_normal),
            Spacer(1, 15),
            Paragraph("STUDENT STRENGTH REPORT", centered_heading),
            Spacer(1, 20),
            table,
        ]

        doc.build(elements)
        return response