from authentication.models import CustomUser
from config.admin import admin_site

admin_site.register(CustomUser)
