from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..resources.association import SMCMemberResource,AssociationTypeResource,StaffAssociationRoleAssignmentResource,AssociationRoleResource,AssociationResource
from ..models.association import AssociationType,Association,AssociationRole,StaffAssociationRoleAssignment,SMCMember
from django.utils.html import format_html

@admin.register(SMCMember)
class SMCMemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'position', 'gender', 'category', 'contact_number', 'email', "school", 'priority', 'photo_tag')
    list_filter = ("position", "gender", "category", "school")
    search_fields = ("name", "email", "contact_number")
    resource_class = SMCMemberResource

    # 🔹 Photo preview in admin
    def photo_tag(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.photo.url
            )
        return "No Photo"
    photo_tag.short_description = "Photo"


@admin.register(AssociationType)
class AssociationTypeAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    resource_class = AssociationTypeResource


@admin.register(Association)
class AssociationAdmin(ImportExportModelAdmin):
    list_display = ("name", "type", "school")
    list_filter = ("type", "school")
    search_fields = ("name", "school__name")
    resource_class = AssociationResource


@admin.register(AssociationRole)
class AssociationRoleAdmin(ImportExportModelAdmin):
    list_display = ("title", "association")
    list_filter = ("association",)
    search_fields = ("title", "association__name")
    resource_class = AssociationRoleResource


@admin.register(StaffAssociationRoleAssignment)
class StaffAssociationRoleAssignmentAdmin(ImportExportModelAdmin):
    list_display = ("staff", "role", "assigned_on")
    list_filter = ("role__association__type", "role__association__school")
    search_fields = ("staff__name", "role__title", "role__association__name")
    resource_class = StaffAssociationRoleAssignmentResource    

class StaffAssociationRoleAssignmentInline(admin.TabularInline):
    model = StaffAssociationRoleAssignment
    extra = 1   # number of empty forms displayed
    autocomplete_fields = ["role", "staff"]  # improves usability if you have many records
    show_change_link = True    