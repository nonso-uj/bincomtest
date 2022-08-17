from django.contrib import admin
from .models import Lga, Ward, Party, PollingUnit, Agentname, States
# Register your models here.


admin.site.register(Lga)
admin.site.register(Ward)
admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(Agentname)
admin.site.register(States)