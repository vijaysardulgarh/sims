import datetime
import logging

from import_export import (
    resources,
    fields
)

from apps.students.models import (
    Student
)

from apps.schools.models import (
    School
)

from apps.academics.models import (
    Class,
    Section,
    Medium,
    Stream
)


class StudentResource(resources.ModelResource):

    # =========================================
    # BASIC INFO
    # =========================================

    srn = fields.Field(
        attribute='srn',
        column_name='SRN'
    )

    school_code = fields.Field(
        attribute='school_code',
        column_name='SchoolCode'
    )

    school_name = fields.Field(
        attribute='school_name',
        column_name='SchoolName'
    )

    admission_date = fields.Field(
        attribute='admission_date',
        column_name='Admission Date'
    )

    roll_number = fields.Field(
        attribute='roll_number',
        column_name='Roll Number'
    )

    admission_number = fields.Field(
        attribute='admission_number',
        column_name='Admission Number'
    )

    # =========================================
    # PERSONAL INFO
    # =========================================

    full_name_aadhar = fields.Field(
        attribute='full_name_aadhar',
        column_name='FullName as on Aadhar Card'
    )

    date_of_birth = fields.Field(
        attribute='date_of_birth',
        column_name='Date of Birth'
    )

    gender = fields.Field(
        attribute='gender',
        column_name='Gender'
    )

    aadhaar_number = fields.Field(
        attribute='aadhaar_number',
        column_name='Aadhaar Number (If any)'
    )

    domicile_of_haryana = fields.Field(
        attribute='domicile_of_haryana',
        column_name='Domicile Of Haryana?'
    )

    # =========================================
    # PARENTS
    # =========================================

    father_full_name_aadhar = fields.Field(
        attribute='father_full_name_aadhar',
        column_name="Father's Full Name aso on Aadhar Card"
    )

    father_aadhaar_number = fields.Field(
        attribute='father_aadhaar_number',
        column_name="Father's Aadhaar Number"
    )

    mother_full_name_aadhar = fields.Field(
        attribute='mother_full_name_aadhar',
        column_name="Mother's Full Name as on Aadhaar"
    )

    mother_aadhaar_number = fields.Field(
        attribute='mother_aadhaar_number',
        column_name="Mother's Aadhaar Number"
    )

    father_mobile = fields.Field(
        attribute='father_mobile',
        column_name="Father's Mobile No"
    )

    mother_mobile = fields.Field(
        attribute='mother_mobile',
        column_name="Mother's Mobile No"
    )

    # =========================================
    # FINANCIAL
    # =========================================

    family_annual_income = fields.Field(
        attribute='family_annual_income',
        column_name='Family Annual Income'
    )

    account_number = fields.Field(
        attribute='account_number',
        column_name='Account Number'
    )

    bank_name = fields.Field(
        attribute='bank_name',
        column_name='Bank Name'
    )

    ifsc = fields.Field(
        attribute='ifsc',
        column_name='IFSC'
    )

    # =========================================
    # SUBJECTS
    # =========================================

    subjects_opted = fields.Field(
        attribute='subjects_opted',
        column_name='Subjects opted by student'
    )

    subjects = fields.Field(
        attribute='subjects',
        column_name='Processed Subjects'
    )

    # =========================================
    # OTHER DETAILS
    # =========================================

    caste = fields.Field(
        attribute='caste',
        column_name='Caste Name'
    )

    category = fields.Field(
        attribute='category',
        column_name='Category Name'
    )

    disability = fields.Field(
        attribute='disability',
        column_name='Disability'
    )

    disorder = fields.Field(
        attribute='disorder',
        column_name='Disorder Name'
    )

    family_id = fields.Field(
        attribute='family_id',
        column_name='FamilyId'
    )

    religion = fields.Field(
        attribute='religion',
        column_name='Religion Name'
    )

    # =========================================
    # META
    # =========================================

    class Meta:

        model = Student

        import_id_fields = [
            'school_code',
            'srn'
        ]

    # =========================================
    # BEFORE IMPORT
    # =========================================

    def before_import(self, dataset, **kwargs):

        excel_school_srn_map = {}

        for row in dataset.dict:

            school_code = row.get('SchoolCode')

            srn = row.get('SRN')

            if school_code and srn:

                excel_school_srn_map.setdefault(
                    school_code,
                    set()
                ).add(srn)

        for school_code, excel_srns in excel_school_srn_map.items():

            existing_srns = set(

                Student.objects.filter(
                    school_code=school_code
                ).values_list(
                    'srn',
                    flat=True
                )
            )

            srns_to_delete = existing_srns - excel_srns

            if srns_to_delete:

                Student.objects.filter(

                    school_code=school_code,

                    srn__in=srns_to_delete

                ).delete()

    # =========================================
    # BEFORE IMPORT ROW
    # =========================================

    def before_import_row(self, row, **kwargs):

        try:

            # =====================================
            # DATE FORMATTING
            # =====================================

            if row.get("Date of Birth"):

                row["Date of Birth"] = self.reformat_date(
                    row["Date of Birth"]
                )

            if row.get("Admission Date"):

                row["Admission Date"] = self.reformat_date(
                    row["Admission Date"]
                )

            # =====================================
            # CLASS CONVERSION
            # =====================================

            class_mapping = {

                "First": "1ST",
                "Second": "2ND",
                "Third": "3RD",
                "Fourth": "4TH",
                "Fifth": "5TH",

                "Sixth": "6TH",
                "Seventh": "7TH",
                "Eighth": "8TH",

                "Ninth": "9TH",
                "Tenth": "10TH",

                "Eleventh": "11TH",
                "Twelfth": "12TH",
            }

            excel_class = row.get("Class")

            if excel_class in class_mapping:

                row["Class"] = class_mapping[
                    excel_class
                ]

            # =====================================
            # SECTION + MEDIUM SPLIT
            # =====================================

            excel_section = row.get("Section")

            if excel_section:

                if "(" in excel_section:

                    section_name = (
                        excel_section
                        .split("(")[0]
                        .strip()
                    )

                    medium_name = (
                        excel_section
                        .split("(")[1]
                        .replace(")", "")
                        .strip()
                    )

                    row["Section"] = section_name

                    row["Medium"] = medium_name

        except Exception as e:

            logging.error(
                f"before_import_row error: {e}"
            )

    # =========================================
    # BEFORE SAVE INSTANCE
    # =========================================

    def before_save_instance(

        self,
        instance,
        row,
        **kwargs
    ):

        # =====================================
        # SCHOOL
        # =====================================

        school_name = row.get("SchoolName")

        school = None

        if school_name:

            school = School.objects.filter(
                name=school_name
            ).first()

            instance.school = school

        # =====================================
        # CLASS
        # =====================================

        class_name = row.get("Class")

        student_class = None

        if class_name:

            student_class = Class.objects.filter(
                name=class_name
            ).first()

            instance.student_class = student_class

        # =====================================
        # STREAM
        # =====================================

        stream_name = row.get("Stream")

        stream = None

        if stream_name:

            stream = Stream.objects.filter(
                name=stream_name
            ).first()

            instance.stream = stream

        # =====================================
        # MEDIUM
        # =====================================

        medium_name = row.get("Medium")

        medium = None

        if medium_name:

            medium = Medium.objects.filter(
                name=medium_name
            ).first()

            instance.medium = medium

        # =====================================
        # SECTION
        # =====================================

        section_name = row.get("Section")

        if section_name and student_class:

            section_query = Section.objects.filter(

                name=section_name,

                class_obj=student_class
            )

            if medium:

                section_query = section_query.filter(
                    medium=medium
                )

            if stream:

                section_query = section_query.filter(
                    stream=stream
                )

            section = section_query.first()

            instance.section = section

    # =========================================
    # DATE FORMATTER
    # =========================================

    def reformat_date(self, date_str):

        try:

            original_format = "%Y-%m-%d"

            date_obj = datetime.datetime.strptime(
                str(date_str),
                original_format
            )

            return date_obj.strftime("%Y-%m-%d")

        except Exception:

            try:

                original_format = "%b %d, %Y"

                date_obj = datetime.datetime.strptime(
                    str(date_str),
                    original_format
                )

                return date_obj.strftime("%Y-%m-%d")

            except Exception as e:

                logging.error(
                    f"Date parsing error: {e}"
                )

                return None