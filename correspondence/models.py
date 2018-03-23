from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


class Ordonnance(models.Model):

    patient = models.ForeignKey('clinic.Patient', on_delete=models.CASCADE)
    ordonnance_date = models.DateField("Date", default=timezone.now())
    medoc1 = models.CharField(max_length=50, blank=True, null=True)
    poso1 = models.CharField(max_length=25, blank=True, null=True)
    qsp1 = models.CharField(max_length=10, blank=True, null=True)
    medoc2 = models.CharField(max_length=50, blank=True, null=True)
    poso2 = models.CharField(max_length=25, blank=True, null=True)
    qsp2 = models.CharField(max_length=10, blank=True, null=True)
    medoc3 = models.CharField(max_length=50, blank=True, null=True)
    poso3 = models.CharField(max_length=25, blank=True, null=True)
    qsp3 = models.CharField(max_length=10, blank=True, null=True)
    medoc4 = models.CharField(max_length=50, blank=True, null=True)
    poso4 = models.CharField(max_length=25, blank=True, null=True)
    qsp4 = models.CharField(max_length=10, blank=True, null=True)
    medoc5 = models.CharField(max_length=50, blank=True, null=True)
    poso5 = models.CharField(max_length=25, blank=True, null=True)
    qsp5 = models.CharField(max_length=10, blank=True, null=True)
    medoc6 = models.CharField(max_length=50, blank=True, null=True)
    poso6 = models.CharField(max_length=25, blank=True, null=True)
    qsp6 = models.CharField(max_length=10, blank=True, null=True)
    medoc7 = models.CharField(max_length=50, blank=True, null=True)
    poso7 = models.CharField(max_length=25, blank=True, null=True)
    qsp7 = models.CharField(max_length=10, blank=True, null=True)
    medoc8 = models.CharField(max_length=50, blank=True, null=True)
    poso8 = models.CharField(max_length=25, blank=True, null=True)
    qsp8 = models.CharField(max_length=10, blank=True, null=True)
    medoc9 = models.CharField(max_length=50, blank=True, null=True)
    poso9 = models.CharField(max_length=25, blank=True, null=True)
    qsp9 = models.CharField(max_length=10, blank=True, null=True)
    medoc10 = models.CharField(max_length=50, blank=True, null=True)
    poso10 = models.CharField(max_length=25, blank=True, null=True)
    qsp10 = models.CharField(max_length=10, blank=True, null=True)
    medoc11 = models.CharField(max_length=50, blank=True, null=True)
    poso11 = models.CharField(max_length=25, blank=True, null=True)
    qsp11 = models.CharField(max_length=10, blank=True, null=True)
    medoc12 = models.CharField(max_length=50, blank=True, null=True)
    poso12 = models.CharField(max_length=25, blank=True, null=True)
    qsp12 = models.CharField(max_length=10, blank=True, null=True)
    medoc13 = models.CharField(max_length=50, blank=True, null=True)
    poso13 = models.CharField(max_length=25, blank=True, null=True)
    qsp13 = models.CharField(max_length=10, blank=True, null=True)
    medoc14 = models.CharField(max_length=50, blank=True, null=True)
    poso14 = models.CharField(max_length=25, blank=True, null=True)
    qsp14 = models.CharField(max_length=10, blank=True, null=True)
    medoc15 = models.CharField(max_length=50, blank=True, null=True)
    poso15 = models.CharField(max_length=25, blank=True, null=True)
    qsp15 = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):

        return '%s -- ordonnance %s' % (self.patient, self.ordonnance_date)


class Certificat(models.Model):
    #
    patient = models.ForeignKey('clinic.Patient', on_delete=models.CASCADE)
    correspondant = models.CharField("Correspondant", max_length=50,
                                     blank=True, null=True)
    certificat_date = models.DateField("Date", default=timezone.now())
    motif = models.ForeignKey('clinic.Motif', blank=True, null=True,
                              on_delete=models.CASCADE)
    declaration = models.CharField("Déclare que", max_length=255,
                                   blank=True, null=True)
    closing = models.CharField("Closing", max_length=100,
                               blank=True, null=True)

    def __str__(self):

        return '%s -- certificat %s' % (self.patient, self.certificat_date)


class Courrier(models.Model):
    #
    patient = models.ForeignKey('clinic.Patient', on_delete=models.CASCADE)
    correspondant = models.CharField("Correspondant", max_length=50,
                                     blank=True, null=True)
    correspondant_adress = models.CharField("Adresse du correspondant",
                                            max_length=100, blank=True,
                                            null=True)
    SALUTATION_CHOICES = (
                     ('C', 'Cher confrère'),
                     ('A', 'Cher ami'),
                     ('S', 'Chère consoeur'),
                     ('B', 'Cher confrère, chère consoeur'),
                     ('M', 'Cher maître'),
                )
    salutation = models.CharField("Salutation", max_length=1,
                                  choices=SALUTATION_CHOICES, default='C')
    courrier_date = models.DateField("Date", default=timezone.now())
    reponse = models.BooleanField(default=False)
    diagnostic = models.CharField(verbose_name="Motif", max_length=100,
                                  blank=True, null=True)
    declaration = models.TextField("l'examen retrouve",
                                   blank=True, null=True)
    conclusion = models.CharField("Conclusion", max_length=255,
                                  blank=True, null=True)
    closing = models.CharField("Closing", max_length=100,
                               blank=True, null=True)

    def __str__(self):

        return '%s courrier %s - %s' % (self.patient, self.courrier_date,
                                        self.correspondant)


class Stomato(models.Model):
    patient = models.ForeignKey('clinic.Patient', on_delete=models.CASCADE)
    stomato_date = models.DateField("Date", default=timezone.now())
    diagnostic = models.CharField("Diagnostic", max_length=100,
                                  blank=True, null=True)
    dentist = models.CharField("Dentiste", max_length=100,
                               blank=True, null=True)
    dentist_adress = models.CharField("Adresse du dentiste", max_length=100,
                                      blank=True, null=True)
    SALUTATION_CHOICES = (
                     ('C', 'Cher confrère'),
                     ('A', 'Cher ami'),
                     ('S', 'Chère consoeur'),
                     ('B', 'Cher confrère, chère consoeur'),
                     ('M', 'Cher maître'),
                )
    salutation = models.CharField("Salutation", max_length=1,
                                  choices=SALUTATION_CHOICES, default='C')

    RISK_CHOICES = (
                     ('F', 'faible'),
                     ('M', 'modéré'),
                     ('I', 'important'),
                )
    infectious_risk = models.CharField(verbose_name="Risque infectieux",
                                       max_length=1, choices=RISK_CHOICES,
                                       default='F')
    thrombotic_risk = models.CharField(verbose_name="Risque thrombo-embolique",
                                       max_length=1, choices=RISK_CHOICES,
                                       default='F')
    syncopal_risk = models.CharField(verbose_name="Risque syncopal",
                                     max_length=1, choices=RISK_CHOICES,
                                     default='F')
    inr_cible = models.DecimalField(verbose_name="INR Cible", max_digits=3,
                                    decimal_places=2, default=1.00)
    lovenox = models.PositiveSmallIntegerField(default=6000)
    avk_interruption = models.NullBooleanField()
    atb = models.NullBooleanField(verbose_name="antibioprophylaxie",
                                  default=False)
    atb_therapie = models.CharField("Antbiothérapie", max_length=255,
                                    blank=True, null=True)

    def __str__(self):

        return '%s stomato %s' % (self.patient, self.stomato_date)


class Arret(models.Model):
    # arret de travail et reprises
    patient = models.ForeignKey('clinic.Patient', on_delete=models.CASCADE)
    arret_date = models.DateField("Date du début", default=timezone.now())
    ARRET_CHOICES = (
                     ('A', 'arrêt de travail'),
                     ('P', 'prolongation'),
                     ('R', 'reprise'),
                )
    type_arret = models.CharField(verbose_name="Type de certifict",
                                  max_length=1, choices=ARRET_CHOICES)
    duree = models.PositiveSmallIntegerField("durée", blank=True, null=True)
    redaction_date = models.DateField("délivré le", default=timezone.now())

    def __str__(self):

        return '%s %s' % (self.patient, self.redaction_date)
