from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..resources.common import FAQResource
from ..models.common import FAQ

@admin.register(FAQ)
class FAQAdmin(ImportExportModelAdmin):  # inherit ImportExportModelAdmin
    resource_class = FAQResource

    list_display = ("question", "category", "is_active", "order", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("question", "answer")
    ordering = ("order", "category")
    list_editable = ("is_active", "order")

    fieldsets = (
        (None, {
            "fields": ("question", "answer", "category", "order", "is_active")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    # Auto-populate order if not set
    def save_model(self, request, obj, form, change):
        if not obj.order:  # if order not set
            max_order = FAQ.objects.filter(category=obj.category).aggregate(admin.models.Max("order"))["order__max"]
            obj.order = (max_order or 0) + 1
        super().save_model(request, obj, form, change)