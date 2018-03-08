from django.contrib import admin
from django.http import HttpResponse
import csv
import datetime
from .models import *

# Register your models here.
class CoronarographieAdmin(admin.ModelAdmin):

        list_display = ("patient","intervention_date","operateur", "emergency")
        list_filter = ('patient', 'intervention_date', 'operateur')
#        search_fields = ('procedure','decision')

class StimulationAdmin(admin.ModelAdmin):

        list_display = ("patient","intervention_date","operateur", "emergency")
        list_filter = ('patient', 'intervention_date', 'operateur')
#        search_fields = ('name','phone')

admin.site.register(Coronarographie, CoronarographieAdmin)
admin.site.register(Stimulation, StimulationAdmin)
admin.site.register(Lesion)
admin.site.register(Indication)
admin.site.register(Complication)
admin.site.register(Guidwire)
admin.site.register(Ballon)
admin.site.register(Stent)
admin.site.register(Pace)
admin.site.register(Sonde)
