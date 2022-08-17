from django.contrib import admin
from .models import AnnouncedLgaResults, AnnouncedPuResults, AnnouncedStateResults, AnnouncedWardResults
# Register your models here.

admin.site.register(AnnouncedLgaResults)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)