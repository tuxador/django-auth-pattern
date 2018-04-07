from django.contrib import admin
from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.utils.html import format_html
from .models import *
from django.http import HttpResponse
import csv
import datetime


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
# for obj in queryset:
#             row = [getattr(obj, field)() if callable(getattr(obj, field)) else getattr(obj, field) for field in field_names]

class PatientAdmin(admin.ModelAdmin):

        # prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("name", "birth", "adresse", "phone",
                        "first_consultation")
#        readonly_fields = ("show_url",)
        #list_filter = ('adresse', 'gender', 'assurance')
        search_fields = ('name', 'phone')
        prepopulated_fields = {'slug': ('name', 'birth')}
        actions = [export_to_csv]

#        def show_url(self, instance):
#            url = reverse("clinics:detail_patient",
#                          kwargs={"pk": instance.pk})
#            response = format_html("""<a href="{0}">{1}</a>""", url, url)
#            return response
#        show_url.short_description = "Patient URL"
#        show_url.allow_tags = True

class ConsultationAdmin(admin.ModelAdmin):

        list_display = ("patient", "medecin", "consultation_date", "emergency",
                        "dispositions", "ordonnance")
    #   list_filter = ('consultation_date', 'emergency', 'medecin', 'patient',)
        date_hierarchy = 'consultation_date'
        actions = [export_to_csv]


class AdmissionAdmin(admin.ModelAdmin):

        list_display = ("patient", "medecin", "admission_date",
                        "emergency", "resume", "dispositions")
    #   list_filter = ('consultation_date', 'emergency', 'medecin', 'patient',)
        date_hierarchy = 'admission_date'
        actions = [export_to_csv]


class ReceptionAdmin(admin.ModelAdmin):

        list_display = ("number", "patient", "date",
                        "planned", "confirmed", "display_prestations")
    # list_filter = ('consultation_date', 'emergency', 'medecin', 'patient',)
        date_hierarchy = 'date'
        actions = [export_to_csv]


class StressAdmin(admin.ModelAdmin):

        list_display = ("patient", "referent", "stress_date", "maximale",
                        "conclusion", "disposition")
        list_filter = ('stress_date', 'patient')
        actions = [export_to_csv]


class FicheTechniqueAdmin(admin.ModelAdmin):

        list_display = ("patient", "date_fiche", "diagnostic",
                        "pathologies_assoc", "risk")
    # list_filter = ('consultation_date', 'emergency', 'medecin', 'patient',)
        date_hierarchy = 'date_fiche'
        actions = [export_to_csv]



admin.site.register(Patient, PatientAdmin)
admin.site.register(Reception, ReceptionAdmin)
admin.site.register(Motif)
admin.site.register(Prestation)
admin.site.register(Wilaya)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Stress, StressAdmin)
admin.site.register(FicheTechnique, FicheTechniqueAdmin)
admin.site.register(Tag)
