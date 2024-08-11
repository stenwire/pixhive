from django.contrib import admin

admin.autodiscover()

class PixhiveAdminSite(admin.AdminSite):
    site_header = "Pixhive Administration"
    site_title = "Pixhive"
    index_title = "Pixhive Administration"
    empty_value_display = "- - - -"


admin_site = PixhiveAdminSite(name="Pixhive Admin Site")