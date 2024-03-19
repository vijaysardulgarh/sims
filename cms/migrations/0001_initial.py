# Generated by Django 5.0.3 on 2024-03-18 15:02

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
            name='CommitteeMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_schedule', models.CharField(blank=True, max_length=100)),
                ('agenda', models.TextField(blank=True)),
                ('location', models.CharField(max_length=100)),
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
                ('established_date', models.DateField(blank=True)),
                ('principal_name', models.CharField(blank=True, max_length=255)),
                ('mission_statement', models.TextField(blank=True)),
                ('vision_statement', models.TextField(blank=True)),
                ('motto', models.CharField(blank=True, max_length=255)),
                ('social_media_links', models.TextField(blank=True)),
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
            name='TimetableSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
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
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('6', '6th'), ('7', '7th'), ('8', '8th'), ('9', '9th'), ('10', '10th'), ('11', '11th'), ('12', '12th')], max_length=50, unique=True)),
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
                ('name', models.CharField(choices=[('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D')], max_length=2)),
                ('section_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='cms.class')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=255)),
                ('mother_name', models.CharField(blank=True, max_length=255)),
                ('spouse_name', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('category', models.CharField(blank=True, choices=[('GEN', 'General'), ('SC', 'Scheduled Caste'), ('ST', 'Scheduled Tribe'), ('OBC', 'Other Backward Class'), ('EWS', 'Economically Weaker Section'), ('OTHER', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField(blank=True)),
                ('joining_date', models.DateField(blank=True)),
                ('retirement_date', models.DateField(blank=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='staff_profile/')),
                ('staff_role', models.CharField(choices=[('teaching', 'Teaching'), ('non_teaching', 'Non-Teaching')], max_length=20)),
                ('employment_type', models.CharField(choices=[('regular', 'Regular'), ('ssa', 'SSA'), ('guest', 'Guest'), ('hkrnl', 'HKRNL'), ('other', 'Other')], max_length=20)),
                ('bio', models.TextField(blank=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff', to='cms.school')),
            ],
            options={
                'ordering': ['employment_type', 'staff_role'],
            },
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
        migrations.AddField(
            model_name='committee',
            name='chairperson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chaired_committees', to='cms.staff'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('courses', models.ManyToManyField(blank=True, related_name='students', to='cms.class')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='cms.school')),
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
                'unique_together': {('section', 'slot')},
            },
        ),
    ]