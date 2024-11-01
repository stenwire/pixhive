from django.contrib import admin

from config.admin import admin_site

from .models import Images


class ImagesAdmin(admin.ModelAdmin):
    list_display = [
        "uuid",
        "original_file_name",
        "file_name",
        "file_type",
        "collection",
        "uploaded_by",
        "upload_finished_at",
        "created",
    ]
    search_fields = [
        "original_file_name",
        "file_name",
        "collection__name",
        "uploaded_by__username",
    ]
    list_filter = [
        "file_type",
        "collection",
        "uploaded_by",
        "upload_finished_at",
        "created",
    ]
    readonly_fields = [
        "uuid",
        "file_url",
        "created",
        "last_updated",
        "file_name",
        "file_type",
        "uploaded_by",
        "upload_finished_at",
        "original_file_name",
    ]
    ordering = ["-created"]

    # def has_add_permission(self, request):
    #     # Disable manual addition of Images through
    # the admin interface, since uploads are managed via API.
    #     return False


admin_site.register(Images, ImagesAdmin)
