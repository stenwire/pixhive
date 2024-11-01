from django.contrib import admin

from accounts.models import Collector, Hiver
from config.admin import admin_site


class HiverAdmin(admin.ModelAdmin):
    list_display = ("user", "created")
    list_filter = ("user", "created")
    search_fields = ("user", "created")


class CollectorAdmin(admin.ModelAdmin):
    list_display = ("user", "created")
    list_filter = ("user", "created")
    search_fields = ("user", "created")


admin_site.register(Hiver, HiverAdmin)
admin_site.register(Collector, CollectorAdmin)
