from django.db import models



class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    srn = models.CharField(primary_key=True, max_length=11)
    school_code = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)
    studentclass = models.CharField(max_length=20, blank=True, null=True)
    stream = models.CharField(max_length=50, blank=True, null=True)
    section = models.CharField(max_length=20, blank=True, null=True)
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


class StudentAchievement(models.Model):
    ACHIEVEMENT_TYPE_CHOICES = [ 
        ("sports", "Sports"),
        ("cultural", "Cultural Activity"),
        ("competition", "Competition"),
        ("exam", "Final Exam"),
        ("quiz", "Quiz"),
    ]

    student_name = models.CharField(max_length=200, help_text="Enter student name")
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPE_CHOICES)
    event_name = models.CharField(max_length=200, blank=True, null=True, help_text="Name of event/activity/exam")
    rank = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 1st, 2nd, Winner")
    reward_title = models.CharField(max_length=200, blank=True, null=True, help_text="Certificate/Medal/Award Title")
    date = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.achievement_type} ({self.event_name or self.reward_title})"



class ExamDetail(models.Model):
    achievement = models.OneToOneField(
        StudentAchievement,
        on_delete=models.CASCADE,
        related_name="exam_detail"
    )
    obtained_marks = models.DecimalField(max_digits=7, decimal_places=2)
    total_marks = models.DecimalField(max_digits=7, decimal_places=2)

    @property
    def percentage(self):
        if self.total_marks > 0:
            return round((self.obtained_marks / self.total_marks) * 100, 2)
        return 0

    def __str__(self):
        return f"{self.achievement.student_name} - {self.obtained_marks}/{self.total_marks} ({self.percentage}%)"