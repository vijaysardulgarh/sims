
from django.shortcuts import render, redirect
from cms.utils import get_current_school
from ..models.student import Student
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table, TableStyle, Spacer, PageBreak,Image
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from ..enrollment_subjects_utils import get_student_cbse_subjects, get_medium_from_section
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, landscape
from collections import defaultdict
import datetime

def signin_link(request):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # ✅ distinct combinations of class and section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # ✅ Define custom order for classes
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # ✅ Sort by studentclass (custom order) then section (alphabetically)
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(
        request,
        "reports/signin_link.html",
        {
            "class_sections": class_sections,
            "school": school  # ✅ also send school to template
        }
    )


def signin(request, class_name, section_name):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)  # optional logo

    # Filter students
    # Filter students and sort by roll_number
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="attendance_{class_name}_{section_name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    # Custom styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    heading_style = ParagraphStyle(name="Heading", fontSize=14, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header: Logo + School Name + Address ---
    header_table_data = []

    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10)
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info Box ---
    subject_class = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200]
    )
    subject_class.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(subject_class)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [["SRN", "Roll No", "Student's Name", "Sub 1", "Sub 2", "Sub 3", "Sub 4", "Sub 5", "Sub 6", "Sub 7"]]

    # --- Student rows ---
    for idx, student in enumerate(students, start=1):
        data.append([
            student.srn,
            student.roll_number,
            student.full_name_aadhar,
            "", "", "", "", "", "", ""
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[60, 50, 200, 60, 60, 60, 60, 60, 60, 60])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor('#AED6F1')),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (1,-1), "CENTER"),
        ("ALIGN", (2,0), (2,-1), "LEFT"),
        ("ALIGN", (3,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # Alternate row background
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # --- Footer with signature lines ---
    footer_data = [
        ["Class Teacher Signature: ______________________", "", "Principal Signature: ______________________"]
    ]
    footer_table = Table(footer_data, colWidths=[250, 100, 250])
    footer_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 20)
    ]))
    elements.append(footer_table)

    # --- Page number function ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response


def roll_call_link(request):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # ✅ distinct combinations of class and section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # ✅ Define custom order for classes
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # ✅ Sort by studentclass (custom order) then section (alphabetically)
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(request, "reports/roll_call_link.html", {"class_sections": class_sections, "school": school})


def roll_call(request, class_name, section_name):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)

    # Filter students
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # PDF Response
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

    # Custom styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header: Logo + School Name ---
    header_table_data = []
    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info ---
    subject_class = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200],
    )
    subject_class.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(subject_class)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [[
        "SRN", "Roll No", "Adm No", "Student's Name",
        "DOB", "Gender", "Aadhaar No",
        "Father's Name", "Mother's Name", "Mobile No.", "Category"
    ]]

    # --- Student Rows ---
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

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[50, 30, 40, 100, 70, 50, 80, 100, 100, 80, 70])
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

    # Alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)

    # --- Page numbers ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response




def subject_report_link(request):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # distinct class-section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # custom order
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # sort by class (custom) then section
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(request, "reports/subject_report_link.html", {
        "class_sections": class_sections,
        "school": school
    })


# ✅ Generate subject report PDF
def subject_report(request, class_name, section_name):
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, 'address', '')
    school_logo = getattr(school, 'logo', None)

    # fetch students
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # response PDF
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="subject_report_{class_name}_{section_name}.pdf"'

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20,
    )

    elements = []
    styles = getSampleStyleSheet()

    # styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header ---
    header_table_data = []
    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info ---
    subject_class = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200],
    )
    subject_class.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(subject_class)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [[
        "SRN", "Roll No",
        "Student's Name", "Subjects"
    ]]

    # --- Student Rows ---
    for student in students:
        data.append([
            student.srn,
            student.roll_number,
            student.full_name_aadhar,
            student.subjects if student.subjects else ""
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[60, 50, 150, 400])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#F9E79F")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (3,-1), "CENTER"),
         ("ALIGN", (2,0), (2,-1), "LEFT"),     # Student's Name left-aligned
        ("ALIGN", (4,0), (5,-1), "LEFT"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)

    # --- Page numbers ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response

def bank_report_link(request):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    # ✅ distinct combinations of class and section for this school
    class_sections = (
        Student.objects.filter(school_name=school)
        .values("studentclass", "section")
        .distinct()
    )

    # ✅ Define custom order for classes
    class_order = ["Sixth", "Seventh", "Eighth", "Nineth", "Tenth", "Eleventh", "Twelfth"]
    order_map = {name: i for i, name in enumerate(class_order)}

    # ✅ Sort by studentclass (custom order) then section (alphabetically)
    class_sections = sorted(
        class_sections,
        key=lambda cs: (order_map.get(cs["studentclass"], 999), cs["section"])
    )

    return render(request, "reports/bank_report_link.html", {"class_sections": class_sections, "school": school})


def bank_report(request, class_name, section_name):
    # ✅ Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")

    school_name = school.name
    school_address = getattr(school, "address", "")
    school_logo = getattr(school, "logo", None)

    # ✅ Filter students
    students = Student.objects.filter(
        school_name=school.name,
        studentclass=class_name,
        section=section_name
    ).order_by("roll_number")

    # ✅ PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="bank_report_{class_name}_{section_name}.pdf"'

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

    # ✅ Custom styles
    school_style = ParagraphStyle(name="SchoolTitle", fontSize=18, alignment=1, spaceAfter=4, fontName="Helvetica-Bold")
    normal_center = ParagraphStyle(name="NormalCenter", alignment=1)

    # --- Header: Logo + School Name ---
    header_table_data = []
    if school_logo:
        logo = Image(school_logo.path, width=50, height=50)
        header_table_data.append([logo, Paragraph(f"<b>{school_name}</b>", school_style), ""])
    else:
        header_table_data.append(["", Paragraph(f"<b>{school_name}</b>", school_style), ""])

    header_table = Table(header_table_data, colWidths=[60, 600, 60])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ]))
    elements.append(header_table)

    if school_address:
        elements.append(Paragraph(school_address, normal_center))
    elements.append(Spacer(1, 12))

    # --- Class Info ---
    subject_class = Table(
        [[f"Class: {class_name}", f"Section: {section_name}", f"Date: {datetime.date.today().strftime('%d-%m-%Y')}"]],
        colWidths=[200, 200, 200],
    )
    subject_class.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,-1), colors.lightgrey),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(subject_class)
    elements.append(Spacer(1, 12))

    # --- Table Header ---
    data = [[
        "SRN", "Roll No", "Student's Name",
        "Aadhaar No", "Bank Name","Account Number", "IFSC", "Family ID","Category"
    ]]

    # --- Student Rows ---
    for student in students:
        data.append([
            student.srn,
            
            student.roll_number,
            student.full_name_aadhar,
            student.aadhaar_number,
            
            student.bank_name,
            
            student.account_number,
            student.ifsc,
            student.family_id,
            student.category,
        ])

    # --- Table Styling ---
    table = Table(data, repeatRows=1, colWidths=[50, 40, 100, 90, 240, 80, 70, 60,40])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#F9E79F")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (3,-1), "CENTER"),
        ("ALIGN", (2,0), (2,-1), "LEFT"),
        ("ALIGN", (4,0), (-1,-1), "LEFT"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("BOX", (0,0), (-1,-1), 1, colors.black),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    # Alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            table.setStyle(TableStyle([("BACKGROUND", (0,i), (-1,i), colors.whitesmoke)]))

    elements.append(table)

    # --- Page numbers ---
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawString(750, 15, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return response



def cwsn_students_report(request):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")


    CLASS_ORDER = {
        "Sixth": 6,
        "Seventh": 7,
        "Eighth": 8,
        "Nineth": 9,
        "Tenth": 10,
        "Eleventh": 11,
        "Twelfth": 12,
    }

    students = list(Student.objects.filter(
        school_name=school.name
    ).exclude(disability__isnull=True).exclude(disability__exact=""))

    students.sort(
        key=lambda s: (
            CLASS_ORDER.get(s.studentclass, 99),
            s.section or "",
            s.roll_number or 0
        )
    )
    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="cwsn_students_{school.name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(name="Title", fontSize=16, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    elements.append(Paragraph(f"CWSN Students Report - {school.name}", title_style))
    elements.append(Spacer(1, 12))

    # Table Header
    data = [[
        "SRN", "Class", "Section", "Roll No", "Adm No", "Student's Name",
        "Father's Name", "DOB", "Gender", "Disability"
    ]]

    # Rows
    for s in students:
        data.append([
            s.srn,
            s.studentclass,
            s.section,
            s.roll_number,
            s.admission_number,
            s.full_name_aadhar,
            s.father_full_name_aadhar,
            s.date_of_birth.strftime("%d-%m-%Y") if s.date_of_birth else "",
            s.gender,
            s.disability,
        ])


    # Table
    table = Table(data, repeatRows=1, colWidths=[60, 50, 50, 40, 60, 100, 100, 70, 50, 150])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(table)

    doc.build(elements)
    return response


def bpl_students_report(request):
    # Get current school
    school = get_current_school(request)
    if not school:
        return redirect("/")


    CLASS_ORDER = {
        "Sixth": 6,
        "Seventh": 7,
        "Eighth": 8,
        "Nineth": 9,
        "Tenth": 10,
        "Eleventh": 11,
        "Twelfth": 12,
    }

    students = list(Student.objects.filter(
        school_name=school.name
    ).exclude(below_poverty_line_certificate_number__isnull=True).exclude(below_poverty_line_certificate_number__exact=""))

    students.sort(
        key=lambda s: (
            CLASS_ORDER.get(s.studentclass, 99),
            s.section or "",
            s.roll_number or 0
        )
    )


    # PDF Response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="bpl_students_{school.name}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    elements = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(name="Title", fontSize=16, alignment=1, spaceAfter=10, fontName="Helvetica-Bold")
    elements.append(Paragraph(f"BPL Students Report - {school.name}", title_style))
    elements.append(Spacer(1, 12))

    # Table Header
    data = [[
        "SRN", "Class", "Section", "Roll No", "Student's Name",
        "DOB", "Gender", "Account No.", "Family ID","BPL Certificate No.","Category",
    ]]

    # Rows
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

    # Table
    table = Table(data, repeatRows=1, colWidths=[60, 50, 50, 40, 100, 70, 50, 90, 60,80,50])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#AED6F1")),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("FONTSIZE", (0,0), (-1,-1), 8),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(table)

    doc.build(elements)
    return response





def generate_student_strength_pdf(request):
    # -------------------------------------------------
    # 🔹 Mapping of DB values -> Display
    # -------------------------------------------------
    class_mapping = {
        "sixth": "6th",
        "seventh": "7th",
        "eighth": "8th",
        "nineth": "9th",
        "ninth": "9th",   # ✅ handle both spellings
        "tenth": "10th",
        "eleventh": "11th",
        "twelfth": "12th",
    }

    # Natural order for sorting
    class_order = {
        c: i for i, c in enumerate(
            ["sixth", "seventh", "eighth", "nineth", "ninth", "tenth", "eleventh", "twelfth"]
        )
    }

    category_list = ["SC", "BC-A", "BC-B", "GEN"]

    # -------------------------------------------------
    # 📊 Group students by class-section
    # -------------------------------------------------
    section_data = defaultdict(lambda: [0] * 8)  # [SC_M, SC_F, BCA_M, BCA_F, BCB_M, BCB_F, GEN_M, GEN_F]

    students = Student.objects.exclude(studentclass__isnull=True).exclude(section__isnull=True)

    for student in students:
        cls = (student.studentclass or "").strip().lower()
        sec = (student.section or "NA").strip().upper()
        gender = (student.gender or "").strip().lower()
        category = (student.category or "").strip().upper()

        if cls not in class_mapping:
            continue  # skip classes outside 6th–12th

        if category not in category_list:
            category = "GEN"  # fallback if unknown

        base_index = category_list.index(category) * 2
        if gender == "male":
            section_data[(cls, sec)][base_index] += 1
        elif gender == "female":
            section_data[(cls, sec)][base_index + 1] += 1
        else:
            section_data[(cls, sec)][base_index] += 1  # default to male col

    # -------------------------------------------------
    # 🏷️ Helper to build table data (class-wise sorting)
    # -------------------------------------------------
    def build_table_data(classes_subset):
        # Header rows
        data = [
            ["Class", "Section",
             "SC", "", "", "BCA", "", "", "BCB", "", "", "GEN", "", "", "Grand Total"],
            ["", "", "Male", "Female", "Total",
             "Male", "Female", "Total",
             "Male", "Female", "Total",
             "Male", "Female", "Total",
             "Total"],
        ]

        block_total = [0] * 8

        # ✅ loop classes in correct order
        for cls in sorted(classes_subset, key=lambda c: class_order.get(c, 999)):
            class_total = [0] * 8

            # all sections for this class
            for (cur_cls, sec), counts in sorted(
                section_data.items(),
                key=lambda x: x[0][1]  # sort sections alphabetically
            ):
                if cur_cls != cls:
                    continue

                sc_total = counts[0] + counts[1]
                bca_total = counts[2] + counts[3]
                bcb_total = counts[4] + counts[5]
                gen_total = counts[6] + counts[7]
                grand_total = sc_total + bca_total + bcb_total + gen_total

                data.append([
                    class_mapping.get(cur_cls, cur_cls), sec,
                    counts[0], counts[1], sc_total,
                    counts[2], counts[3], bca_total,
                    counts[4], counts[5], bcb_total,
                    counts[6], counts[7], gen_total,
                    grand_total
                ])

                # accumulate into class total
                class_total = [a+b for a, b in zip(class_total, counts)]

            # ✅ add total row for this class
            if sum(class_total) > 0:
                sc_total = class_total[0] + class_total[1]
                bca_total = class_total[2] + class_total[3]
                bcb_total = class_total[4] + class_total[5]
                gen_total = class_total[6] + class_total[7]
                grand_total = sc_total + bca_total + bcb_total + gen_total

                data.append([
                    f"Total {class_mapping.get(cls, cls)}", "",
                    class_total[0], class_total[1], sc_total,
                    class_total[2], class_total[3], bca_total,
                    class_total[4], class_total[5], bcb_total,
                    class_total[6], class_total[7], gen_total,
                    grand_total
                ])

                # add into block total
                block_total = [a+b for a, b in zip(block_total, class_total)]

        # ✅ finally block total
        sc_total = block_total[0] + block_total[1]
        bca_total = block_total[2] + block_total[3]
        bcb_total = block_total[4] + block_total[5]
        gen_total = block_total[6] + block_total[7]
        grand_total = sc_total + bca_total + bcb_total + gen_total

        data.append([
            f"Total ({', '.join(class_mapping[c] for c in classes_subset if c in class_mapping)})", "",
            block_total[0], block_total[1], sc_total,
            block_total[2], block_total[3], bca_total,
            block_total[4], block_total[5], bcb_total,
            block_total[6], block_total[7], gen_total,
            grand_total
        ])

        return data, block_total

    # -------------------------------------------------
    # 📌 Prepare PDF
    # -------------------------------------------------
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="student_strength.pdf"'

    page_width, page_height = landscape(A4)
    doc = SimpleDocTemplate(
        response,
        pagesize=(page_width, page_height),
        leftMargin=20, rightMargin=20,
        topMargin=20, bottomMargin=20
    )

    elements = []
    styles = getSampleStyleSheet()

    # -------------------------------------------------
    # Page 1 → 6th to 8th
    # -------------------------------------------------
    elements.append(Paragraph("<b>Student Strength Report (6th to 8th)</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    data_6_8, total_6_8 = build_table_data(["sixth", "seventh", "eighth"])
    col_widths = [50, 50] + [40] * (len(data_6_8[0]) - 2)

    table1 = Table(data_6_8, colWidths=col_widths, repeatRows=2)
    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("BACKGROUND", (0, 1), (-1, 1), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 1), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

        # spans
        ("SPAN", (0, 0), (0, 1)),  # Class
        ("SPAN", (1, 0), (1, 1)),  # Section
        ("SPAN", (2, 0), (4, 0)),  # SC
        ("SPAN", (5, 0), (7, 0)),  # BCA
        ("SPAN", (8, 0), (10, 0)), # BCB
        ("SPAN", (11, 0), (13, 0)),# GEN
        ("SPAN", (14, 0), (14, 1)),# Grand Total

        ("BACKGROUND", (0, -1), (-1, -1), colors.lightgrey),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
    ])
    table1.setStyle(style)
    elements.append(table1)

    elements.append(PageBreak())

    # -------------------------------------------------
    # Page 2 → 9th to 12th
    # -------------------------------------------------
    elements.append(Paragraph("<b>Student Strength Report (9th to 12th)</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    data_9_12, total_9_12 = build_table_data(["ninth", "nineth", "tenth", "eleventh", "twelfth"])
    table2 = Table(data_9_12, colWidths=col_widths, repeatRows=2)
    table2.setStyle(style)
    elements.append(table2)

    # -------------------------------------------------
    # Optional Grand Total across 6th–12th
    # -------------------------------------------------
    grand_total = [a+b for a, b in zip(total_6_8, total_9_12)]
    sc_total = grand_total[0] + grand_total[1]
    bca_total = grand_total[2] + grand_total[3]
    bcb_total = grand_total[4] + grand_total[5]
    gen_total = grand_total[6] + grand_total[7]
    all_total = sc_total + bca_total + bcb_total + gen_total

    data_grand = [[
        "Grand Total (6th–12th)", "",
        grand_total[0], grand_total[1], sc_total,
        grand_total[2], grand_total[3], bca_total,
        grand_total[4], grand_total[5], bcb_total,
        grand_total[6], grand_total[7], gen_total,
        all_total
    ]]

    table3 = Table(data_grand, colWidths=col_widths)
    table3.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    elements.append(Spacer(1, 12))
    elements.append(table3)

    # -------------------------------------------------
    # Build PDF
    # -------------------------------------------------
    doc.build(elements)
    return response


# -------------------------------
# CBSE Enrollment PDF View
# -------------------------------
def cbse_enrollment_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cbse_enrollment.pdf"'

    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
    doc = SimpleDocTemplate(response, pagesize=landscape(A4), leftMargin=10, rightMargin=10, topMargin=15, bottomMargin=15)
    elements = []
    styles = getSampleStyleSheet()
    normal_style = ParagraphStyle("normal", fontSize=6, leading=7, alignment=1)

    headers = [
        "CLASS","SECTION","ROLL_NO","CAT","CNAME","MNAME","FNAME",
        "SEX","CAST","HANDICAP",
        "SUB1","SUB2","SUB3","SUB4","SUB5","SUB6","SUB7",
        "D_O_B","ANNUAL_INC","ONLY_CHILD","ADM_SRL","ADM_DATE","MINORITY"
    ]
    data = [[Paragraph(h, normal_style) for h in headers]]

    minority_religions = {"MUSLIM", "CHRISTIAN", "SIKH", "BUDDHIST", "JAIN", "PARSI"}
    students = Student.objects.filter(studentclass__in=["Ninth", "Eleventh"]).order_by("studentclass", "section", "roll_number")

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
            s.admission_number or "", s.admission_date.strftime("%d-%m-%Y") if s.admission_date else "",
            minority_flag
        ]

        data.append([Paragraph(str(c) if c else " ", normal_style) for c in row])

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

# -------------------------------
# CBSE Enrollment CSV
# -------------------------------
def cbse_enrollment_csv(request):
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
    students = Student.objects.filter(studentclass__in=["Ninth", "Eleventh"]).order_by("studentclass", "section", "roll_number")

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