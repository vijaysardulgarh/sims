# Generated by Django 5.0.3 on 2024-04-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_staff_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bpl_certificate_issuing_authority',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
