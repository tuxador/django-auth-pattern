from django.db import models
from datetime import datetime
from django.utils import timezone
# from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
# from clinic.models import Patient avoid circular import
# between patient-prestation-quotation
# Create your models here.

class Quotation(models.Model):
    acte = models.CharField("Acte médical", max_length=100)
    code = models.CharField("Code", max_length=15)

    def __str__(self):
        return(self.acte)



class Convention(models.Model):
    patient = models.ForeignKey('clinic.Patient', related_name='conventions',
                                on_delete=models.CASCADE) 
    code = models.CharField("Code patient", max_length=100,
                            blank=True, null=True)
    date_depot = models.DateField("date depôt dossier",
                                  default=timezone.now())
    date_maj = models.DateField("date MAJ  dossier",
                                auto_now_add=True)
    traitement = models.TextField("Traitement")
    quotation = models.ManyToManyField("quotation", blank=True, null=True)
    Remarque = models.CharField("Remarque", max_length=255,
                                null=True, blank=True)
# dossier administratif
    attestation_droit = models.NullBooleanField("Attestation ouverture droits")
    debut_validite = models.DateField("Début de validité attestation",
                                      blank=True, null=True)
    fin_validite = models.DateField("Fin  validité attestation",
                                    blank=True, null=True)
    photocopies = models.BooleanField("Photocopie", default=True)
    extrait_naissance = models.BooleanField("extrait de naissance enfant",
                                            default=False)
    kafala = models.BooleanField("Kafala", default=True)
    fiche_familiale = models.BooleanField("Fiche familiale", default=True)
# dossier médical
    telethorax = models.DateField("Téléthorax", blank=True, null=True)
    ecg = models.DateField("ECG", blank=True, null=True)
    ett = models.DateField("Echocoeur", blank=True, null=True)
    epreuve_effort = models.DateField("épreuve d'effort", blank=True,
                                      null=True)
    stress_echo = models.DateField("Stress-echo", blank=True, null=True)
    scintigraphie = models.DateField("Scintigraphie myocardique", blank=True,
                                     null=True)
    coroscan = models.DateField("Coroscanner", blank=True, null=True)
    doppler_tsa = models.DateField("Doppler des TSA", blank=True, null=True)
    doppler_mi = models.DateField("Doppler des MI", blank=True, null=True)
    coro_repport = models.DateField("CD + compte rendu de coro",
                                    null=True, blank=True)
    echo_abdom = models.DateField("échographie abdominale",
                                  null=True, blank=True)
    efr = models.DateField("EFR", null=True, blank=True)
    stomato = models.DateField("Expertise dentaire", null=True, blank=True)
# biologie
    glycemie = models.DateField("Glycémie", null=True, blank=True)
    hba1c = models.DateField("Hemoglobine glycquée",
                             null=True, blank=True)
    coro_repport = models.DateField("CD + compte rendu de coro",
                                    null=True, blank=True)
    uree_creat = models.DateField("Urée - Créatinine",
                                  null=True, blank=True)
    lipidogramme = models.DateField("Lipidogramme",
                                    null=True, blank=True)
    crp = models.DateField("CRP", null=True, blank=True)
    vs = models.DateField("VS", null=True, blank=True)
    tp_inr = models.DateField("TP - INR", null=True, blank=True)
    tca = models.DateField("TCA", null=True, blank=True)
    groupage = models.DateField("Groupage phénotypé", null=True, blank=True)
    hiv = models.DateField("Sérologie HIV", null=True, blank=True)
    hcv = models.DateField("Sérologie HCV", null=True, blank=True)
    hbv = models.DateField("Sérologie HBV", null=True, blank=True)
    rejet = models.DateField("Rejet le", null=True, blank=True)

    def __str__(self):
        return f'{self.patient} : {self.code} - deposé le {self.date_depot}'


class Prestation(models.Model):
    acte = models.CharField(verbose_name="acte médical",
                            max_length=50)
    codification = models.CharField(verbose_name="codification", max_length=15,
                                    blank=True, null=True)
    tarif = models.PositiveSmallIntegerField("tarif", blank=True, null=True)

    def __str__(self):
        return(self.acte)
