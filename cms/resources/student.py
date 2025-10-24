from import_export import resources, fields
from ..models.student import Student
import datetime
import logging

class StudentResource(resources.ModelResource):
   
    srn = fields.Field(attribute='srn', column_name='SRN')
    school_code = fields.Field(attribute='school_code', column_name='SchoolCode')
    school_name = fields.Field(attribute='school_name', column_name='SchoolName')
    admission_date = fields.Field(attribute='admission_date', column_name='Admission Date')
    studentclass = fields.Field(attribute='studentclass', column_name='Class')
    stream = fields.Field(attribute='stream', column_name='Stream')
    section = fields.Field(attribute='section', column_name='Section')
    roll_number = fields.Field(attribute='roll_number', column_name='Roll Number')
    admission_number = fields.Field(attribute='admission_number', column_name='Admission Number')
 
    # Personal Info

    full_name_aadhar = fields.Field(attribute='full_name_aadhar', column_name='FullName as on Aadhar Card')
    # name_in_local_language = fields.Field(attribute='name_in_local_language', column_name='Name In Local Language')
    date_of_birth = fields.Field(attribute='date_of_birth', column_name='Date of Birth')
    gender = fields.Field(attribute='gender', column_name='Gender')
    aadhaar_number = fields.Field(attribute='aadhaar_number', column_name='Aadhaar Number (If any)')
    domicile_of_haryana = fields.Field(attribute='domicile_of_haryana', column_name='Domicile Of Haryana?')

    # Parents / Guardian

    father_full_name_aadhar = fields.Field(attribute='father_full_name_aadhar', column_name="Father's Full Name aso on Aadhar Card")
    father_aadhaar_number = fields.Field(attribute='father_aadhaar_number', column_name="Father's Aadhaar Number")
    mother_full_name_aadhar = fields.Field(attribute='mother_full_name_aadhar', column_name="Mother's Full Name as on Aadhaar")
    mother_aadhaar_number = fields.Field(attribute='mother_aadhaar_number', column_name="Mother's Aadhaar Number")

    # Contact

    father_mobile = fields.Field(attribute='father_mobile', column_name="Father's Mobile No")
    mother_mobile = fields.Field(attribute='mother_mobile', column_name="Mother's Mobile No")

    # Financial
    family_annual_income = fields.Field(attribute='family_annual_income', column_name='Family Annual Income')
    account_number = fields.Field(attribute='account_number', column_name='Account Number')
    bank_name = fields.Field(attribute='bank_name', column_name='Bank Name')
    ifsc = fields.Field(attribute='ifsc', column_name='IFSC')

    # Subjects
    subjects_opted = fields.Field(attribute='subjects_opted', column_name='Subjects opted by student')
    subjects = fields.Field(attribute='subjects', column_name='Processed Subjects')  # ✅ your cleaned subjects logic

    caste = fields.Field(attribute='caste', column_name='Caste Name')
    category = fields.Field(attribute='category', column_name='Category Name')
    disability = fields.Field(attribute='disability', column_name='Disability')
    disorder = fields.Field(attribute='disorder', column_name='Disorder Name')
    bpl_certificate_issuing_authority = fields.Field(attribute='bpl_certificate_issuing_authority', column_name='BPL Certificate Issuing Authority')
    below_poverty_line_certificate_number = fields.Field(attribute='below_poverty_line_certificate_number', column_name='Below Poverty Line Certificate Number')
    
    family_id = fields.Field(attribute='family_id', column_name='FamilyId') 
    religion = fields.Field(attribute='religion', column_name='Religion Name')

    class Meta:
        model = Student
        import_id_fields = ['school_code','srn']
        export_order = ( 
            'srn', 
            'school_code', 
            'school_name', 
            'admission_date',
            'studentclass', 
            'stream', 
            'section', 
            'roll_number', 
            'admission_number',

            # Personal Info
             'full_name_aadhar', 
            # 'name_in_local_language',
             'date_of_birth', 
             'gender', 
             'aadhaar_number', 
             'domicile_of_haryana', 

            # Parents / Guardian
            'father_full_name_aadhar', 
            'father_aadhaar_number', 
            'mother_full_name_aadhar', 
            'mother_aadhaar_number',

            # Contact
            'father_mobile',
            'mother_mobile',

            # Financial
            'family_annual_income', 
            'account_number',
            'bank_name',
            'ifsc',

            # Subjects
             'subjects_opted', 
             'subjects',

             'caste',
             'category',
             'disability',
             'disorder',
             'bpl_certificate_issuing_authority',
             'below_poverty_line_certificate_number',
             'family_id',
             'religion'
             
        )
    def before_import(self, dataset, **kwargs):
        # Collect all SRNs grouped by school_code from the Excel file
        excel_school_srn_map = {}
        for row in dataset.dict:
            school_code = row.get('SchoolCode')
            srn = row.get('SRN')
            if school_code and srn:
                excel_school_srn_map.setdefault(school_code, set()).add(srn)

        # For each school in the Excel file, delete only the students of that school
        for school_code, excel_srns in excel_school_srn_map.items():
            # Get all existing SRNs for this school
            existing_srns = set(
                Student.objects.filter(school_code=school_code).values_list('srn', flat=True)
            )

            # Find SRNs that need to be deleted (only within this school)
            srns_to_delete = existing_srns - excel_srns

            if srns_to_delete:
                Student.objects.filter(school_code=school_code, srn__in=srns_to_delete).delete()
      
            
    def before_import_row(self, row, **kwargs):
        try:
            if 'Date of Birth' in row and row['Date of Birth']:
                row['Date of Birth'] = self.reformat_date(row['Date of Birth'])
            if 'Admission Date' in row and row['Admission Date']:
                row['Admission Date'] = self.reformat_date(row['Admission Date'])
        except ValueError as e:
            logging.error(f"Error converting date: {e}. Row: {row}")

    def reformat_date(self, date_str):
        try:
            original_format = "%b %d, %Y"  # Adjust format for date with time
            date_obj = datetime.datetime.strptime(date_str, original_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error parsing date '{date_str}': {e}")
            return None  # Or provide a default value