from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from cms.models.school import Infrastructure,AboutSchool,Principal,Affiliation,MandatoryPublicDisclosure,School
from cms.resources.school import InfrastructureResource,AboutSchoolResource,AffiliationResource,PrincipalResource,SchoolResource
from django.utils.html import format_html

@admin.register(Infrastructure)
class InfrastructureAdmin(ImportExportModelAdmin):
    list_display = ("title", "school", "category", "photo_tag")
    list_filter = ("category", "school")
    search_fields = ("title", "school__name", "description")
    resource_class = InfrastructureResource

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="70" height="50" style="object-fit:cover;border-radius:4px;"/>',
                obj.photo.url,
            )
        return "-"
    photo_tag.short_description = "Photo"





@admin.register(AboutSchool)
class AboutSchoolAdmin(ImportExportModelAdmin):
    list_display = ("school", "short_history", "short_vision", "short_mission")
    search_fields = ("school__name", "history", "vision", "mission")
    resource_class = AboutSchoolResource

    def short_history(self, obj):
        return (obj.history[:50] + "...") if obj.history else "-"
    short_history.short_description = "History"

    def short_vision(self, obj):
        return (obj.vision[:50] + "...") if obj.vision else "-"
    short_vision.short_description = "Vision"

    def short_mission(self, obj):
        return (obj.mission[:50] + "...") if obj.mission else "-"
    short_mission.short_description = "Mission"


@admin.register(Principal)
class PrincipalAdmin(ImportExportModelAdmin):
    list_display = ("name", "school", "photo_tag", "short_message")
    search_fields = ("name", "school__name", "message")
    resource_class = PrincipalResource

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover;border-radius:50%;"/>',
                obj.photo.url,
            )
        return "-"
    photo_tag.short_description = "Photo"

    def short_message(self, obj):
        return (obj.message[:60] + "...") if obj.message else "-"
    short_message.short_description = "Message"


@admin.register(Affiliation)
class AffiliationAdmin(ImportExportModelAdmin):
    list_display = ("name", "school", "short_description")
    search_fields = ("name", "school__name", "description")
    resource_class = AffiliationResource

    def short_description(self, obj):
        return (obj.description[:60] + "...") if obj.description else "-"
    short_description.short_description = "Description"


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "school", "uploaded_at")
    search_fields = ("title", "school__name")


@admin.register(School)
class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource
    list_display = ("name", "email", "phone_number", "established_date")
    search_fields = ("name", "email", "phone_number")
    list_filter = ("established_date", "accreditation")    

@admin.register(MandatoryPublicDisclosure)
class MandatoryPublicDisclosureAdmin(ImportExportModelAdmin):
    list_display = ("section", "title", "value", "file", "order", "is_active")
    list_filter = ("section", "is_active")
    search_fields = ("title", "value")
    ordering = ("section", "order")   