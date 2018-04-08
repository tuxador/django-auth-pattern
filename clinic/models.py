from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from billing.models import Prestation
# Create your models here.


class Wilaya(models.Model):
    wilaya = models.CharField(max_length=25)
    code = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return(self.wilaya)


class Motif(models.Model):
    motif = models.CharField(verbose_name="motif d'admission",
                             max_length=25)

    def __str__(self):
        return(self.motif)


class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=True)

    def __str__(self):
            return(self.tag)


class Patient(models.Model):
    name = models.CharField(verbose_name="Nom et prénoms",
                            max_length=50)
    slug = models.SlugField(max_length=100)
    birth = models.DateField(verbose_name="date de naissance")
    birth_place = models.ForeignKey(Wilaya,
                                    verbose_name="lieu de naisssance",
                                    on_delete=models.CASCADE,
                                    related_name='originaires',
                                    blank=True, null=True)
    GENDER_CHOICES = (
                     ('M', 'Masculin'),
                     ('F', 'Féminin'),
                     ('O', 'autre'),
                )
    gender = models.CharField(verbose_name="sexe",
                              max_length=1, choices=GENDER_CHOICES)
    adresse = models.ForeignKey(Wilaya, on_delete=models.CASCADE,
                                related_name='demeurants', blank=True,
                                null=True)
    phone = models.CharField("Téléphone", max_length=10,
                             default='0550123456')
    PROFESSION_CHOICES = (
                     ('F', 'fonctionnaire'),
                     ('E', 'employé'),
                     ('C', 'commerçant'),
                     ('R', 'retraité'),
                     ('Y', 'femme au foyer'),
                     ('T', 'étudiant'),
                     ('S', 'scolarisé'),
                     ('D', 'cadre'),
                     ('L', 'profession libérale'),
                     ('O', 'au chômage'),
                )
    profession = models.CharField(verbose_name="Profession",
                                  max_length=1,
                                  choices=PROFESSION_CHOICES,
                                  blank=True)

    ASSURANCE_CHOICES = (
                     ('N', 'CNAS'),
                     ('S', 'CASNOS'),
                     ('A', 'Autre'),
                     ('O', 'Non assuré'),
                )
    assurance = models.CharField(verbose_name="Assurance sociale",
                                 max_length=1,
                                 choices=ASSURANCE_CHOICES,
                                 default='N')
    correspondant = models.CharField("Médecin correspondant",
                                     max_length=255, blank=True)
    first_consultation = models.DateField("première consultation",
                                          default=timezone.now)
# antécedents et FDR
    hypertension = models.BooleanField("hypertendu(e)", default=True)
    diabete = models.BooleanField("diabétique", default=True)
    dyslipidemia = models.BooleanField("dyslipidémie", default=True)
    smoker = models.BooleanField("tabagique", default=False)
    weight = models.PositiveSmallIntegerField(verbose_name="poids",
                                              blank=True)
    lenght = models.DecimalField(verbose_name="taille", max_digits=3,
                                 decimal_places=2, default=1.70)
# bmi = weight/lenght*lenght
    body_area = models.DecimalField(verbose_name="surface corporelle",
                                    max_digits=3, decimal_places=2, default=1.70)
    obesity = models.BooleanField("obèse", default=True)
    sedentarity = models.BooleanField("sédentarité", default=True)
    heredity = models.BooleanField("hérédité coronarienne",
                                   default=False)
    history = models.TextField("antécedents")
    surgery_history = models.TextField("antécédents de chirurgie cardique ou de geste interventionne", blank=True)
    allergy = models.CharField("allergie connue", max_length=50,
                               blank=True)
    tags = models.ManyToManyField(Tag, default="cardio")

#  def save(self, *args, **kwargs):
#                  super(Patient, self).save(*args, **kwargs)
#                  if not self.slug:
#                            self.slug = slugify("%s %s",(self.name,self.id))
#                                 self.save()
    class Meta:
        ordering = ['name']

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, self.birth)
        super().save()

    def __str__(self):

        return(self.slug)


class Consultation(models.Model):
    #   données générales et symptomatologie
    patient = models.ForeignKey(Patient, related_name='consults',
                                on_delete=models.CASCADE)
    consultation_date = models.DateField("date de consultation")
    medecin = models.ForeignKey(User,
                                blank=True, on_delete=models.CASCADE)
    emergency = models.BooleanField("urgence", default=False)
    motif_consultation = models.ManyToManyField(Motif)
    med_ref = models.CharField("Médecin réfferent", max_length=100,
                               blank=True, null=True)
    fever = models.BooleanField("fièvre", default=False)
    dyspnea_nyha = models.PositiveSmallIntegerField("stade NYHA",
                                                    default='1')
    angina_scc = models.PositiveSmallIntegerField("stade d'angor",
                                                  default='1')
    syncope = models.BooleanField("Syncope", default=False)
    histoire = models.CharField("Histoire de la maladie",
                                max_length=255, null=True, blank=True)
#
# examen clinique
    systolic_bp = models.PositiveSmallIntegerField(blank=True,
                                                   null=True)
    diastolic_bp = models.PositiveSmallIntegerField(blank=True,
                                                    null=True)
    heart_rate = models.PositiveSmallIntegerField(blank=True,
                                                  null=True)
    auscultation = models.CharField(max_length=100, blank=True,
                                    null=True)
    ivg = models.BooleanField(default=False)
    ivd = models.BooleanField(default=False)
    pulse = models.CharField(max_length=50, blank=True)
    telethorax = models.CharField(max_length=150, blank=True, null=True)
#
#    # ECG

    RYTHM_CHOICES = (
        ('S', 'Sinusal'),
        ('F', 'Atrial Fibrillation'),
        ('R', 'Atrial Flutter'),
        ('P', 'Pace Maker'),
        ('T', 'TV')
    )
    rythm = models.CharField(max_length=1, choices=RYTHM_CHOICES,
                             blank=True, null=True)
    freq = models.PositiveSmallIntegerField(default='70')
    BLOCK_CHOICES = (
        ('D', 'BBD'),
        ('G', 'BBG')
        )
    bundle_block = models.CharField(max_length=1,
                                    choices=BLOCK_CHOICES, blank=True,
                                    null=True)
    hypertrophy = models.NullBooleanField(default=False)
    TERRITORY = (
        ('N', 'Null'),
        ('S', 'Septal'),
        ('A', 'Anterior'),
        ('L', 'Lateral'),
        ('P', 'Posterior'),
    )
    necrosis = models.CharField(max_length=1, choices=TERRITORY,
                                blank=True, null=True)
    ischaemia = models.CharField(max_length=1, choices=TERRITORY,
                                 blank=True, null=True)
    lesion = models.CharField(max_length=1, choices=TERRITORY,
                              blank=True, null=True)
    t_inversion = models.CharField(max_length=1, choices=TERRITORY,
                                   blank=True, null=True)
    corrected_qt = models.IntegerField(default=400)
# echocoeur
    echocoeur = models.TextField("échocardiographie", null=True,
                                 blank=True)
    date_echo = models.DateField("Date de l'écho",
                                 default=timezone.now)
    eto = models.TextField("échocardiographie trans-oesophagienne",
                           null=True, blank=True)
    fevg = models.PositiveSmallIntegerField("FeVG", blank=True,
                                            null=True)
# evolution
    resume = models.TextField("résumé clinique", null=True)
# ordonnance de sortie
    dispositions = models.CharField("dispositions complémentaires",
                                    max_length=255, blank=True)
    ordonnance = models.TextField("ordonnance", blank=True, null=True)

    def __str__(self):

        return '%s %s' % (self.patient, self.consultation_date)
    # def get_absolute_url(self):
    #    return reverse('detail_consultation', kwargs={'pk':self.pk})


class Reception(models.Model):
    patient = models.ForeignKey(Patient, related_name='rendez_vous',
                                on_delete=models.CASCADE)
    date = models.DateField("Date du rendez-vous", blank=True, null=True)
    planned = models.NullBooleanField("patient programmé", default=True)
    confirmed = models.NullBooleanField("Confirmé", default=False)
    number = models.PositiveSmallIntegerField("n°",
                                              blank=True, null=True)
    prestations = models.ManyToManyField(Prestation, null=True, blank=True)
    manque = models.PositiveSmallIntegerField("montant manquant",
                                              blank=True, null=True)
    paid = models.DateField("reglé le", null=True, blank=True)
    reduction = models.NullBooleanField("réduction", default=False)

    def display_prestations(self):
        return '- '.join([prestation.acte for prestation in self.prestations.all()])
    display_prestations.short_description = 'Prestations'
    display_prestations.allow_tags = True

    def __str__(self):
        return f'{self.number}_{self.patient}  RDV: {self.date}'


class Stress(models.Model):
                # données générales et symptomatologie
                #
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stress_date = models.DateField("Date du stress-echo",
                                   default=timezone.now)
    referent = models.CharField("Médecin référent", max_length=50,
                                blank=True)
    medecin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,
                                on_delete=models.CASCADE)
    motif_stress = models.ManyToManyField(Motif)
    medication = models.CharField("traitement habituel",
                                  max_length=255, blank=True)
    dobu_5 = models.NullBooleanField("Dobu 5 gammas")
    dobu_10 = models.NullBooleanField("Dobu 10 gammas")
    dobu_15 = models.NullBooleanField("Dobu 15 gammas")
    dobu_20 = models.NullBooleanField("Dobu 20 gammas")
    dobu_30 = models.NullBooleanField("Dobu 30 gammas")
    dobu_40 = models.NullBooleanField("Dobu 40 gammas")
    atropin_1 = models.NullBooleanField("Atropine 0.25 mg")
    atropin_2 = models.NullBooleanField("Atropine 0.50 mg")
    atropin_3 = models.NullBooleanField("Atropine 0.75 mg")
    atropin_4 = models.NullBooleanField("Atropine 1.00 mg")
    bb_peros = models.NullBooleanField("Beta bloqueur per os")
    bb_iv = models.NullBooleanField("Beta bloqueur IV")
    nitrin = models.NullBooleanField("Dérivés nitrés")
    OBJECTIF_CHOICES = (
        ('I', 'Ischémie'),
        ('V', 'Viabilité'),
        ('R', 'Réserve contractile'),
        ('G', 'Gradient trans-aortique'),
        ('M', 'Fuite mitrale')
    )
    objectif = models.CharField(max_length=1, choices=OBJECTIF_CHOICES)
# examen de base
    base_systolic_bp = models.PositiveSmallIntegerField("PAS base",
                                                        blank=True,
                                                        null=True)
    base_diastolic_bp = models.PositiveSmallIntegerField("PAD base",
                                                         blank=True,
                                                         null=True)
    base_heart_rate = models.PositiveSmallIntegerField("FC base",
                                                       blank=True,
                                                       null=True)
    base_ecg = models.CharField("ECG base", max_length=255,
                                blank=True, null=True)
    base_echo = models.CharField("écho de base", max_length=255,
                                 blank=True, null=True)
# low dose
    low_symptoma = models.CharField("Symptômes low dose",
                                    max_length=255, blank=True,
                                    null=True)
    low_systolic_bp = models.PositiveSmallIntegerField("PAS low dose",
                                                       blank=True,
                                                       null=True)
    low_diastolic_bp = models.PositiveSmallIntegerField("PAD low dose",
                                                        blank=True,
                                                        null=True)
    low_heart_rate = models.PositiveSmallIntegerField("FC low dose",
                                                      blank=True,
                                                      null=True)
    low_ecg = models.CharField("ECG low dose", max_length=255,
                               blank=True, null=True)
    low_echo = models.CharField("écho low dose", max_length=255,
                                blank=True, null=True)
# peak dose
    peak_symptoma = models.CharField("Symptômes peak dose",
                                     max_length=255, blank=True,
                                     null=True)
    peak_systolic_bp = models.PositiveSmallIntegerField("PAS peak dose",
                                                        blank=True,
                                                        null=True)
    peak_diastolic_bp = models.PositiveSmallIntegerField("PAD peak dose",
                                                         blank=True,
                                                         null=True)
    peak_heart_rate = models.PositiveSmallIntegerField("FC peak dose",
                                                       blank=True,
                                                       null=True)
    peak_ecg = models.CharField("ECG peak dose", max_length=255,
                                blank=True, null=True)
    peak_echo = models.CharField("écho peak dose", max_length=255,
                                 blank=True, null=True)
# Récupération
    recup_symptoma = models.CharField("Symptômes récupération",
                                      max_length=255, blank=True,
                                      null=True)
    recup_systolic_bp = models.PositiveSmallIntegerField("PAS récupération",
                                                         blank=True,
                                                         null=True)
    recup_diastolic_bp = models.PositiveSmallIntegerField("PAD récupération",
                                                          blank=True,
                                                          null=True)
    recup_heart_rate = models.PositiveSmallIntegerField("FC récupération",
                                                        blank=True,
                                                        null=True)
    recup_ecg = models.CharField("ECG récupération", max_length=255,
                                 blank=True, null=True)
    recup_echo = models.CharField("écho de récupération",
                                  max_length=255, blank=True,
                                  null=True)
# evolution
    maximale = models.BooleanField("épreuve maximale", default=True)
    conclusion = models.TextField("Conclusion", blank=True)
    DISPOSITION_CHOICES = (
        ('M', 'Traitement médical'),
        ('C', 'Coronarographie diagnostique'),
        ('R', 'Coronarographie et éventuel geste de revascularisation'),
        ('N', 'Non concluante'),
        ('O', 'indication opératoire'),
    )
    disposition = models.CharField("Dispositions complémentaires",
                                   max_length=1,
                                   choices=DISPOSITION_CHOICES,
                                   default='M')

    def __str__(self):

        return '%s stress %s' % (self.patient, self.stress_date)


class Admission(models.Model):
    #   données générales et symptomatologie
    patient = models.ForeignKey(Patient, related_name='admissions',
                                on_delete=models.CASCADE)
    admission_date = models.DateField("date de l'admission")
    medecin = models.ForeignKey(User,
                                blank=True, on_delete=models.CASCADE)
    emergency = models.BooleanField("urgence", default=False)
    motif_admission = models.ManyToManyField(Motif)
    med_ref = models.CharField("Médecin reférent", max_length=100,
                               blank=True, null=True)
    UNITY_CHOICES = (
        ('1', 'salles 1er'),
        ('2', 'salles 2ème'),
        ('3', 'USIC'),
        ('4', 'réanimation'),
    )
    unity = models.CharField("unité d'hospitalisation",
                             max_length=1,
                             choices=UNITY_CHOICES,
                             default='1')

    chambre = models.CharField("Chambre", max_length=5, blank=True)
    fever = models.BooleanField("fièvre", default=False)
    dyspnea_nyha = models.PositiveSmallIntegerField("stade NYHA",
                                                    default='1')
    angina_scc = models.PositiveSmallIntegerField("stade d'angor",
                                                  default='1')
    syncope = models.BooleanField("Syncope", default=False)
    histoire = models.CharField("Histoire de la maladie",
                                max_length=255, null=True, blank=True)
#
# examen clinique
    etat_general = models.CharField("état à l'admision",
                                    max_length=255, blank=True)
    systolic_bp = models.PositiveSmallIntegerField(blank=True,
                                                   null=True)
    diastolic_bp = models.PositiveSmallIntegerField(blank=True,
                                                    null=True)
    heart_rate = models.PositiveSmallIntegerField(blank=True,
                                                  null=True)
    auscultation = models.CharField(max_length=100, blank=True,
                                    null=True)
    ivg = models.BooleanField("signes d'IVG", default=False)
    ivd = models.BooleanField("signes d'IVD", default=False)
    tsj = models.BooleanField("Turguscence des jugulaires", default=False)
    rhj = models.BooleanField("reflux hpato-jugulaire", default=False)
    omi = models.BooleanField("oedèmes des MI", default=False)
    pulse = models.CharField(max_length=50, blank=True)
    telethorax = models.CharField(max_length=50, blank=True, null=True)
#
#    # ECG

    RYTHM_CHOICES = (
        ('S', 'Sinusal'),
        ('F', 'Atrial Fibrillation'),
        ('R', 'Atrial Flutter'),
        ('P', 'Pace Maker'),
        ('T', 'TV')
    )
    rythm = models.CharField("rythme", max_length=1, choices=RYTHM_CHOICES,
                             blank=True, null=True)
    freq = models.PositiveSmallIntegerField("fréquence cardiaque", default='70')
    BLOCK_CHOICES = (
        ('D', 'BBD'),
        ('G', 'BBG')
        )
    bundle_block = models.CharField("Bloc de branche", max_length=1,
                                    choices=BLOCK_CHOICES, blank=True)
    HYPERTROPHY_CHOICES = (
        ('G', 'HVG'),
        ('D', 'HVD')
        )
    hypertrophy = models.CharField("Hypertrophie ventriculaire", max_length=1,
                                   choices=HYPERTROPHY_CHOICES, blank=True)
    TERRITORY = (
        ('N', 'absence'),
        ('S', 'septal'),
        ('A', 'antérieur'),
        ('L', 'latéral'),
        ('P', 'posterieur'),
    )
    necrosis = models.CharField(max_length=1, choices=TERRITORY,
                                blank=True, null=True)
    ischaemia = models.CharField(max_length=1, choices=TERRITORY,
                                 blank=True, null=True)
    lesion = models.CharField(max_length=1, choices=TERRITORY,
                              blank=True, null=True)
    t_inversion = models.CharField(max_length=1, choices=TERRITORY,
                                   blank=True, null=True)
    corrected_qt = models.IntegerField(default=400)
# echocoeur
    echocoeur = models.TextField("échocardiographie", null=True,
                                 blank=True)
    date_echo = models.DateField("Date de l'écho",
                                 default=timezone.now)
    eto = models.TextField("échocardiographie trans-oesophagienne",
                           null=True, blank=True)
    fevg = models.PositiveSmallIntegerField("FeVG", blank=True,
                                            null=True)
# evolution
    resume = models.TextField("Résumé clinique", blank=True)
    evolution = models.TextField("Evolution", blank=True)
# ordonnance de sortie
    sortant = models.NullBooleanField("Sortant")
    sortie_date = models.DateField("Date de sortie", null=True)
    dispositions = models.CharField("dispositions complémentaires",
                                    max_length=255, blank=True)
    ordonnance = models.TextField("Ordonnance", blank=True, null=True)

    def __str__(self):

        return '%s %s' % (self.patient, self.admission_date)
    # def get_absolute_url(self):
    #    return reverse('detail_consultation', kwargs={'pk':self.pk})


class FicheTechnique(models.Model):
    patient = models.ForeignKey(Patient, related_name='fiches_techniques',
                                on_delete=models.CASCADE)
    date_fiche = models.DateField("Date de la fiche", default=timezone.now)
    diagnostic = models.CharField("Diagnostic exact", max_length=255, blank=True)
    pathologies_assoc = models.CharField("Pathologies associées",
                                         max_length=255, blank=True)
    nyha = models.PositiveSmallIntegerField("Stade NYHA", default=1)
    telethorax = models.CharField("Téléthorax", max_length=255, blank=True)
    ecg = models.CharField("ECG", max_length=255, blank=True)
    echocoeur = models.TextField("Echocoeur (conclusion)", blank=True)
    telethorax = models.CharField("Téléthorax", max_length=255, blank=True)
    taille_og = models.CharField("Taille et vacuité de l'OG", max_length=255, blank=True)
    vd = models.CharField("Fonction VD", max_length=255, blank=True)
    fevg = models.PositiveSmallIntegerField("FEVG", null=True, blank=True)
    valvulopathy = models.CharField("Atteinte valvulaire (grade)",
                                    max_length=255, blank=True)
    aorte = models.CharField("État de l'aorte", max_length=255, blank=True)
    TEST = (
            ('E', 'ECG d\'effort'),
            ('S', 'stress-echo'),
            ('M', 'scintigraphie myocardique'),
            ('C', 'Coroscan'),
            ('R', 'IRM cardiaque'),
           )
    test_ischemie = models.CharField("Test d'ischémie", max_length=1,
                                     choices=TEST, blank=True)
    result_test_ischemie = models.CharField("Résultats du test d'ischémie",
                                            max_length=255, blank=True)
    coro = models.CharField("état des coronaires (coronarographie)",
                            max_length=255, blank=True)
    syntax = models.PositiveSmallIntegerField("SYNTAX score",
                                              blank=True, null=True)
    coroscan = models.CharField("état des coronaires (coroscanner)",
                                max_length=255, blank=True)
    periph = models.TextField("état des artères périphériques (doppler ou angio)",
                              blank=True)
    clearance_cr = models.PositiveSmallIntegerField("Fonction rénale (clearance)",
                                                    null=True, blank=True)
    dfg = models.PositiveSmallIntegerField("Fonction rénale (Débit de filtration glomérulaire)",
                                           null=True, blank=True)
    respir = models.CharField("fonction respiratoire",
                              max_length=255, blank=True)
    dentaire = models.CharField("État dentaire",
                                max_length=255, blank=True)
    biology = models.TextField("Biologie: principales anomalies",
                               blank=True)
    traitement = models.TextField("Traitement médical",
                                  blank=True)
    risk = models.TextField("Évaluation du risque opératoire",
                            blank=True)
    def __str__(self):

        return '%s_fiche_%s' % (self.patient, self.date_fiche)
