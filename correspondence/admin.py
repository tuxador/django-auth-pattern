from django.contrib import admin
from .models import *


class CertificatAdmin(admin.ModelAdmin):

        #        prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("patient","certificat_date","correspondant", "motif")
        list_filter = ('patient', 'correspondant', 'certificat_date')
        search_fields = ('patient','certificat_date')

class CourrierAdmin(admin.ModelAdmin):

        #        prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("patient","courrier_date",
                        "correspondant", "diagnostic", "reponse")
        list_filter = ('patient', 'correspondant', 'courrier_date')
        search_fields = ('patient','courrier_date')

class StomatoAdmin(admin.ModelAdmin):

        #        prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("patient","stomato_date","diagnostic",
                        "avk_interruption", "inr_cible", "atb")
        list_filter = ('patient',)
        search_fields = ('patient',)

class ArretAdmin(admin.ModelAdmin):

        #        prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("patient","redaction_date","type_arret", "duree")
        list_filter = ('patient', 'redaction_date', 'arret_date')
        search_fields = ('patient',)
class OrdonnanceAdmin(admin.ModelAdmin):

        #        prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("patient","ordonnance_date")
        list_filter = ('patient', 'ordonnance_date')
        search_fields = ('patient',)


admin.site.register(Certificat, CertificatAdmin)
admin.site.register(Ordonnance, OrdonnanceAdmin)
admin.site.register(Courrier, CourrierAdmin)
admin.site.register(Arret, ArretAdmin)
admin.site.register(Stomato, StomatoAdmin)

# Register your models here.
