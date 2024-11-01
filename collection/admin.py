from django.contrib import admin

from collection.models import Collection
from config.admin import admin_site


class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "is_public", "created")
    list_filter = ("is_public", "created", "last_updated", "owner")
    search_fields = ("is_public", "owner")


admin_site.register(Collection, CollectionAdmin)
