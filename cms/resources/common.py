from import_export import resources, fields
from ..models.common import FAQ
class FAQResource(resources.ModelResource):
    class Meta:
        model = FAQ
        fields = ("id", "question", "answer", "category", "order", "is_active", "created_at", "updated_at")
        export_order = ("id", "question", "answer", "category", "order", "is_active", "created_at", "updated_at")