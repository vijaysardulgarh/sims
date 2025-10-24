from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..models.finance import FeeStructure

@admin.register(FeeStructure)
class FeeStructureAdmin(ImportExportModelAdmin):
    list_display = (
        "student_class",
        "stream",
        "admission_fee_display",
        "rcf_display",
        "cwf_display",
        "ccwf_display",
        "total_fee_display",
    )
    search_fields = ("student_class__name", "stream__name")
    list_filter = ("student_class", "stream")

    def admission_fee_display(self, obj):
        return round(obj.admission_fee)
    admission_fee_display.short_description = "Admission Fee"

    def rcf_display(self, obj):
        return round(obj.rcf)
    rcf_display.short_description = "RCF"

    def cwf_display(self, obj):
        return round(obj.cwf)
    cwf_display.short_description = "CWF"

    def ccwf_display(self, obj):
        return round(obj.ccwf)
    ccwf_display.short_description = "CCWF"

    def total_fee_display(self, obj):
        return round(obj.total_fee())
    total_fee_display.short_description = "Total Fee"