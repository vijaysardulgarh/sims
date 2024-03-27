# Generated by Django 5.0.3 on 2024-03-27 15:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_schedule', models.CharField(blank=True, max_length=100)),
                ('agenda', models.TextField(blank=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='facility_images/')),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='news/')),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['-date_published'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('logo', models.ImageField(blank=True, upload_to='logos/')),
                ('accreditation', models.CharField(blank=True, max_length=255)),
                ('established_date', models.DateField(blank=True, null=True)),
                ('principal_name', models.CharField(blank=True, max_length=255)),
                ('mission_statement', models.TextField(blank=True)),
                ('vision_statement', models.TextField(blank=True)),
                ('motto', models.CharField(blank=True, max_length=255)),
                ('social_media_links', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50)),
                ('mother_name', models.CharField(blank=True, max_length=50)),
                ('spouse_name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('aadhar_number', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('designation', models.CharField(blank=True, max_length=40, null=True)),
                ('category', models.CharField(blank=True, choices=[('GEN', 'General'), ('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe'), ('OBC', 'Other Backward Class'), ('EWS', 'Economically Weaker Section'), ('OTHER', 'Other')], max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('current_joining_date', models.DateField(blank=True, null=True)),
                ('retirement_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15)),
                ('teaching_subject_1', models.CharField(blank=True, max_length=50)),
                ('teaching_subject_2', models.CharField(blank=True, max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='staff_profile/')),
                ('staff_role', models.CharField(choices=[('teaching', 'Teaching'), ('non_teaching', 'Non-Teaching')], max_length=20)),
                ('employment_type', models.CharField(choices=[('regular', 'Regular'), ('ssa', 'SSA'), ('guest', 'Guest'), ('hkrnl', 'HKRNL'), ('nsqf', 'NSQF'), ('mdmworker', 'MDM Worker'), ('other', 'Other')], max_length=20)),
                ('bio', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Staff',
                'ordering': ['employment_type', 'staff_role'],
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts')], max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('srn', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('school_code', models.CharField(blank=True, max_length=20, null=True)),
                ('school_name', models.CharField(blank=True, max_length=255, null=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('studentclass', models.CharField(blank=True, max_length=20, null=True)),
                ('stream', models.CharField(blank=True, max_length=20, null=True)),
                ('section', models.CharField(blank=True, max_length=20, null=True)),
                ('roll_number', models.CharField(blank=True, max_length=20, null=True)),
                ('admission_number', models.CharField(blank=True, max_length=20, null=True)),
                ('full_name_aadhar', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=20, null=True)),
                ('domicile_of_haryana', models.CharField(blank=True, max_length=100, null=True)),
                ('father_full_name_aadhar', models.CharField(blank=True, max_length=255, null=True)),
                ('father_aadhaar_number', models.CharField(blank=True, max_length=20, null=True)),
                ('mother_full_name_aadhar', models.CharField(blank=True, max_length=255, null=True)),
                ('mother_aadhaar_number', models.CharField(blank=True, max_length=20, null=True)),
                ('guardian_full_name_aadhar', models.CharField(blank=True, max_length=255, null=True)),
                ('guardian_aadhaar_number', models.CharField(blank=True, max_length=20, null=True)),
                ('family_annual_income', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('block', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_district', models.CharField(blank=True, max_length=100, null=True)),
                ('city_village_town', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('father_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('mother_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('guardian_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=20, null=True)),
                ('subjects_opted', models.CharField(blank=True, max_length=255, null=True)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('disability', models.CharField(blank=True, max_length=255, null=True)),
                ('disorder', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Hindi', 'Hindi'), ('English', 'English'), ('Social Studies', 'Social Studies'), ('Science', 'Science'), ('Math', 'Math'), ('Punjabi', 'Punjabi'), ('Computer', 'Computer'), ('Home Science', 'Home Science'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Account', 'Account'), ('Business', 'Business'), ('Political Science', 'Political Science'), ('Economics', 'Economics'), ('Geography', 'Geography'), ('Psychology', 'Psychology'), ('Physical Education', 'Physical Education'), ('Music', 'Music'), ('Automobile', 'Automobile'), ('Beauty & Wellness', 'Beauty & Wellness')], max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('objectives', models.TextField(blank=True)),
                ('tasks', models.TextField(blank=True)),
                ('documents', models.ManyToManyField(blank=True, related_name='committee', to='cms.document')),
                ('chairperson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chaired_committees', to='cms.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th'), ('na', 'NA')], max_length=50, unique=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.school')),
            ],
            options={
                'verbose_name_plural': 'Class',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('na', 'NA')], max_length=2)),
                ('section_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='cms.class')),
                ('section_stream', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='cms.stream')),
            ],
        ),
        migrations.CreateModel(
            name='Nodal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('responsibilities', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nodal', to='cms.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('head_of_department', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Department', to='cms.staff')),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('image', models.ImageField(blank=True, upload_to='smc_members/')),
                ('committee', models.ManyToManyField(blank=True, related_name='CommitteeMember', to='cms.committee')),
                ('member', models.ManyToManyField(blank=True, related_name='CommitteeMember', to='cms.staff')),
            ],
            options={
                'ordering': ['designation'],
            },
        ),
        migrations.CreateModel(
            name='ClassIncharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_alloted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.class')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.classroom')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.section')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.staff')),
            ],
        ),
        migrations.CreateModel(
            name='ExtracurricularActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Sports', 'Sports'), ('Clubs', 'Clubs'), ('Arts', 'Arts'), ('Academic', 'Academic'), ('Community Service', 'Community Service'), ('Other', 'Other')], max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='activity_images/')),
                ('requirements', models.TextField(blank=True)),
                ('achievements', models.TextField(blank=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('registration_link', models.URLField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('coordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coordinated_activities', to='cms.staff')),
                ('participants', models.ManyToManyField(blank=True, related_name='participated_activities', to='cms.student')),
            ],
            options={
                'verbose_name_plural': 'Extracurricular Activities',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(choices=[('winter', 'winter'), ('summer', 'Summer'), ('other', 'Other')], max_length=10)),
                ('class_type', models.CharField(choices=[('Regular', 'Regular'), ('Assembly', 'Assembly'), ('Recess', 'Recess'), ('Special', 'Special Event')], default='Regular', max_length=10)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_mandatory', models.BooleanField(default=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Timetable', to='cms.class')),
                ('classrooms', models.ManyToManyField(blank=True, to='cms.classroom')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='timetable', to='cms.section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.subject')),
                ('teachers', models.ManyToManyField(blank=True, to='cms.staff')),
            ],
        ),
        migrations.CreateModel(
            name='TimetableSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.day')),
            ],
        ),
        migrations.CreateModel(
            name='Topper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('obtained_marks', models.FloatField()),
                ('total_marks', models.FloatField()),
                ('exam_date', models.DateField()),
                ('position', models.PositiveIntegerField()),
                ('reason', models.TextField(blank=True, null=True)),
                ('date_awarded', models.DateField(blank=True, null=True)),
                ('award_type', models.CharField(choices=[('Topper', 'Topper'), ('Shining Star', 'Shining Star')], max_length=20, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.student')),
            ],
        ),
        migrations.CreateModel(
            name='TimetableEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.school')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.staff')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.timetableslot')),
            ],
            options={
                'verbose_name_plural': 'Time Table Entries',
                'unique_together': {('section', 'slot')},
            },
        ),
    ]
