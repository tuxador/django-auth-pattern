from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from clinic import Patient
# Create your models here.


class   Complication(models.Model):
                complication = models.CharField(max_length=25)

                def __str__(self):
                    return(self.complication)

class   Indication(models.Model):
                indication = models.CharField(max_length=25)

                def __str__(self):
                    return(self.indication)


class   Lesion(models.Model):
                lesion = models.CharField(max_length=25)

                def __str__(self):
                    return(self.lesion)



class Coroscan(models.Model):

    # données générales et symptomatologie
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    coroscan_date = models.DateField("Date du coroscanner",
                                     default=timezone.now)
    referent = models.CharField("Médecin référent", max_length=50,
                                blank=True, null=True)
    medecin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                                null=True, on_delete=models.CASCADE)
    medication = models.CharField("traitement habituel",
                                  max_length=255, blank=True,
                                  null=True)
    COROSCAN_CHOICES = (
                    ('1', 'Douleur thoracique'),
                    ('2', 'Dysfonction VG'),
                    ('3', 'Pré op'),
                    ('4', 'Contrôle de PAC'),
                    ('5', 'Test d\'ischémie litigieux'),
                    ('6', 'Contrôle de stent'),
                    ('7', 'IMS')
    )
    motif = models.CharField(max_length=1,
                             choices=COROSCAN_CHOICES, null=True,
                             blank=True)
    base_heart_rate = models.PositiveSmallIntegerField("FC base",
                                                       blank=True,
                                                       null=True)
    base_ecg = models.CharField("ECG base", max_length=255,
                                blank=True, null=True)
    quality = models.CharField("Qualité de l'examen",
                               max_length=255, blank=True, null=True)
    voltage = models.CharField(max_length=10, default="100Kv")
    amperage = models.CharField("Ampérage", max_length=10,
                                blank=True, null=True)
    pas = models.CharField("PAS", max_length=10, default="0.35")
    longueur_champ = models.CharField("Longueur champ",
                                      max_length=10, default="16cm")
    ctdivol = models.PositiveSmallIntegerField("CTDIvol",
                                               blank=True, null = True)
    dlp = models.PositiveSmallIntegerField("DLP mgy/cm", blank=True,
                                           null=True)
    tcg = models.CharField("TCG", max_length=255, blank=True,
                           null=True)
    iva = models.CharField("IVA", max_length=255, blank=True,
                           null=True)
    diag = models.CharField("Diagonale", max_length=255,
                            blank=True, null=True)
    bissec = models.CharField("Bissectrice", max_length=255,
                              blank=True, null=True)
    cx = models.CharField("Circonflexe", max_length=255,
                          blank=True, null=True)
    mg = models.CharField("Marginale", max_length=255,
                          blank=True, null=True)
    cd = models.CharField("Coronaire droite",
                          max_length=255, blank=True, null=True)
    ivp = models.CharField("IVP", max_length=255, blank=True,
                           null=True)
    rvg = models.CharField("RVG", max_length=255,
                           blank=True, null=True)
    dominance = models.NullBooleanField("Dominance droite",
                                        default=True)
    calcic_total = models.PositiveSmallIntegerField("score Calcique global",
                                                    default='0')
    calcic_tcg = models.PositiveSmallIntegerField("score Ca TCG",
                                                  default='0')
    calcic_iva = models.PositiveSmallIntegerField("score Ca IVA",
                                                  default='0')
    calcic_diag = models.PositiveSmallIntegerField("score Ca Diag",
                                                   default='0')
    calcic_cx = models.PositiveSmallIntegerField("score Ca Cx",
                                                 default='0')
    calcic_bissec = models.PositiveSmallIntegerField("score Ca Bissectrice",
                                                     default='0')
    calcic_mg = models.PositiveSmallIntegerField("score Ca Mg",
                                                 default='0')
    calcic_cd = models.PositiveSmallIntegerField("score Ca CD",
                                                 default='0')
    calcic_ivp = models.PositiveSmallIntegerField("score Ca IVP",
                                                  default='0')
    cinetic_vg = models.TextField("Cinétique VG", blank=True,
                                  null=True)
    fevg = models.PositiveSmallIntegerField("FeVG", null=True,
                                            blank=True)
    conclusion = models.TextField("Conclusion", blank=True, null=True)

    def __str__(self):

        return 'Coroscan %s -- %s' % (self.patient, self.coroscan_date)



class   Coronarographie(models.Model):

                patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
                intervention_date = models.DateField("date d'intervention")
                operateur = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
                aide = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='intervention_coronarographie_aide')
                emergency = models.BooleanField("urgence", default=False)
                indication = models.ManyToManyField(Indication, blank=True)

                ABORD = (
                    ('R', 'Radial'),
                    ('F', 'Femoral'),
                    ('O', 'Autre'),
                )


                abord = models.CharField("abord artériel", max_length=1, choices=ABORD, default='R', null=True)
                sonde = models.ManyToManyField(Sonde, blank=True)
                guide = models.ManyToManyField(Guidwire, blank=True)
                stent = models.ManyToManyField(Stent, blank = True)
                iode = models.PositiveSmallIntegerField("Produit de contrast", blank=True, null=True)
                tcg = models.CharField(max_length=255, blank=True, null=True)
                iva = models.CharField("IVA", max_length=255, blank=True, null=True)
                iva_prox = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_iva_prox')
                iva_moy = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_iva_moy')
                iva_dist = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_iva_dist')
                bissectrice = models.CharField("Bissectrice", max_length=255, blank=True, null=True)
                bissec = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_bissec')
                circonflexe = models.CharField("Circonflexe", max_length=255, blank=True, null=True)
                cx_prox = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_cx_prox')
                cx_moy = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_cx_moy')
                cx_dist = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_cx_dist')
                marginale = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_marginale')

                coronaire_dte = models.CharField("Coronaire droite", max_length=255, blank=True, null=True)
                cd1 = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_cd1')
                cd2 = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_cd2')
                cd3 = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_cd3')
                ivp = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_ivp')
                rvg = models.ForeignKey(Lesion, blank=True, null=True, related_name='intervention_coronarographie_rvg')
                dominance = models.NullBooleanField(default=True)
                conclusion = models.TextField("Conclusion", blank=True, null=True)
                decision = models.CharField("Décision thérapeutique", max_length=255, blank=True, null=True)
                staff_date = models.DateField("Date du staff", default = timezone.now)

                # partie dédiée à l'angioplastie
                procedure = models.TextField("Angioplastie", blank=True, null=True)
                succes = models.BooleanField(default=True)
                complications = models.ManyToManyField(Complication, blank=True)
                dispositions = models.CharField("Dispositions complémentaires", max_length=255, blank=True)


                def __str__(self):

                    return '%s %s' % (self.patient, self.intervention_date)

                def get_absolute_url(self):
                    return reverse('detail_coronarographie', kwargs={'pk': self.pk})

class   Stimulation(models.Model):

                patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
                intervention_date = models.DateField("date d'intervention")
                operateur = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
                aide = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='intervention_stimulation_aide')
                pacemaker = models.ForeignKey(Pace)
                emergency = models.BooleanField("urgence", default=False)
                indication = models.ManyToManyField(Indication, blank=True)
                epuisement = models.BooleanField("changement de boîtier", default=False)
                type_stimulation = models.CharField("Type de stimulation", max_length=4, blank=True)
                procedure = models.TextField("procédure")
                duree = models.DurationField(null=True, blank=True)
                complications = models.ManyToManyField(Complication, blank=True)
                dispositions = models.CharField("Dispositions complémentaires",max_length=255,  blank=True)


                def __str__(self):

                    return '%s %s' % (self.patient, self.intervention_date)

                def get_absolute_url(self):

                    return reverse('detail_stimulation', kwargs={'pk': self.pk})
                     # return reverse('list_stimulations')
