from django.contrib import admin
from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.utils.html import format_html
from .models import *
from django.http import HttpResponse
import csv
import datetime


# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
                                                         opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

class ConventionAdmin(admin.ModelAdmin):

        list_display = ("patient", "code", "date_depot",
                        "date_maj", "attestation_droit",
                        "debut_validite", "fin_validite", "Remarque")
        list_filter = ('debut_validite', 'fin_validite', 'rejet')
        date_hierarchy = 'date_depot'
        actions = [export_to_csv]


class QuotationAdmin(admin.ModelAdmin):
    list_display = ("code","acte")
    actions= [export_to_csv]
admin.site.register(Convention, ConventionAdmin)
admin.site.register(Quotation, QuotationAdmin)
#admin.site.register(Prestation)
