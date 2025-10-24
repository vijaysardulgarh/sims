from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from ..models.schoolclass import Medium,Classroom,Class,Section,Stream
from ..resources.schoolclass import MediumResource,ClassroomResource,ClassResource,SectionResource,StreamResource

@admin.register(Medium)
class MediumAdmin(ImportExportModelAdmin):
    resource_class = MediumResource
    list_display = ("name", "school")
    search_fields = ("name", "school__name")
    list_filter = ("school",)

@admin.register(Classroom)
class ClassroomAdmin(ImportExportModelAdmin):
    resource_class = ClassroomResource
    list_display = ("name", "school", "capacity", "floor")
    search_fields = ("name", "school__name")
    list_filter = ("school",)

@admin.register(Class)
class ClassAdmin(ImportExportModelAdmin):
    resource_class = ClassResource
    list_display = ("name", "school", "class_order")
    search_fields = ("name", "school__name")
    list_filter = ("school","class_order")

@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    resource_class = SectionResource

    # Show Section fields in the list
    list_display = ("school", "sec_class", "name", "medium", "stream", "sub_stream", "classroom")

    # Filters in sidebar
    list_filter = ("school", "sec_class", "stream", "medium", "sub_stream")

    # Searchable fields
    search_fields = (
        "name",
        "sec_class__name",
        "school__name",
        "classroom__name",
        "stream__name",
        "medium__name",
        "sub_stream"
    )    


@admin.register(Stream)
class StreamAdmin(ImportExportModelAdmin):
    resource_class = StreamResource
    list_display = ('school','name')
    search_fields = ('school','name')    