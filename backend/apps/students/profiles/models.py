from django.db import models

from apps.schools.models import School
from apps.academics.classes.models import Class
from apps.academics.streams.models import Stream
from apps.academics.sections.models import Section
from apps.core.common.base.models import AuditBaseModel
from django.conf import settings

class Student(AuditBaseModel):
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="student_profile"
    )
    srn = models.CharField(primary_key=True, max_length=11)
    school_code = models.CharField(max_length=20, blank=True, null=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name="students")
    
    admission_date = models.DateField(blank=True, null=True)
    student_class = models.ForeignKey(Class,on_delete=models.SET_NULL,related_name="students",null=True,blank=True,db_index=True)
    stream = models.ForeignKey(Stream,on_delete=models.SET_NULL,related_name="students",null=True,blank=True,db_index=True)
    section = models.ForeignKey(Section,on_delete=models.SET_NULL,related_name="students",null=True,blank=True,db_index=True)
    roll_number = models.IntegerField(blank=True, null=True)
    admission_number = models.CharField(max_length=20, blank=True, null=True)

    # Personal Info
    full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    domicile_of_haryana = models.CharField(max_length=100, blank=True, null=True)

    # Parents / Guardian
    father_full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    father_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)
    mother_full_name_aadhar = models.CharField(max_length=255, blank=True, null=True)
    mother_aadhaar_number = models.CharField(max_length=20, blank=True, null=True)


    # Contact
    father_mobile = models.CharField(max_length=20, blank=True, null=True)
    mother_mobile = models.CharField(max_length=20, blank=True, null=True)


    # Financial
    family_annual_income = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)

    # Address
    state = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    sub_district = models.CharField(max_length=100, blank=True, null=True)
    city_village_town = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Subjects
    subjects_opted = models.TextField(blank=True, null=True, help_text="Format: Optional:Math, Compulsory:English")
    subjects = models.TextField(blank=True, null=True)

    caste = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    disability = models.CharField(max_length=255, blank=True, null=True)
    disorder = models.CharField(max_length=100, blank=True, null=True)
    below_poverty_line_certificate_number=models.CharField(max_length=255, blank=True, null=True)
    bpl_certificate_issuing_authority = models.CharField(max_length=255, blank=True, null=True)

    family_id = models.CharField(max_length=50, blank=True, null=True)
    religion=models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        indexes = [
            models.Index(fields=["school"]),
            models.Index(fields=["section"]),
        ]
    def __str__(self):
        return str(self.full_name_aadhar) if self.full_name_aadhar else 'Student {}'.format(self.pk)

    def save(self, *args, **kwargs):
        # --- Normalize category ---
        if self.category:
            normalized = self.category.strip().lower()
            mapping = {
                "sc": "SC",
                "scheduled caste": "SC",
                "gen": "GEN",
                "general": "GEN",
                "bc-a": "BC-A",
                "bca": "BC-A",
                "bc-b": "BC-B",
                "bcb": "BC-B",
                "sbc": "GEN",   # 🔹 Count SBC in General
            }
            self.category = mapping.get(normalized, self.category.upper())

        # --- Normalize subjects_opted ---
        if self.subjects_opted:
            subject_list = str(self.subjects_opted).split(',')
            all_subjects = []

            for subject in subject_list:
                parts = subject.split(':', 1)
                if len(parts) == 2:
                    subject_type, subject_name = parts
                    subject_type = subject_type.strip()
                    subject_name = subject_name.strip()

                    if subject_type in ("Compulsory", "Optional","Optional 1","Optional 2", "NSQF", "Language"):
                        all_subjects.append(subject_name)
                    elif subject_type == "Additional":
                        all_subjects.append(f"Additional: {subject_name}")

            # 🔹 Remove duplicates but preserve order
            seen = {}
            cleaned_subjects = [seen.setdefault(s, s) for s in all_subjects if s not in seen]

            # 🔹 Sort alphabetically (case-insensitive)
            self.subjects = ', '.join(sorted(cleaned_subjects, key=lambda x: x.lower()))
        else:
            self.subjects = None

        # ✅ Always call super().save()
        super().save(*args, **kwargs)