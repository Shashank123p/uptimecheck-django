from django.contrib import admin
from uptime.models import websites
# Register your models here.

class websitesAdmin(admin.ModelAdmin):
    list_display = ('website',)
    search_fields = ('website',)


admin.site.register(websites, websitesAdmin)