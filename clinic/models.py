from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


class Wilaya(models.Model):
    wilaya = models.CharField(max_length=25)

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
    slug = models.SlugField(max_length=100, unique_for_date='birth')
    birth = models.DateField(verbose_name="date de naissance")

    GENDER_CHOICES = (
                     ('M', 'Masculin'),
                     ('F', 'Féminin'),
                )
    gender = models.CharField(verbose_name="sexe",
                              max_length=1, choices=GENDER_CHOICES)
    adresse = models.ForeignKey(Wilaya,
                                on_delete=models.CASCADE, blank=True,
                                null=True)
    phone = models.CharField("Téléphone", max_length=10,
                             default='0550123456')
    PROFESSION_CHOICES = (
                     ('F', 'fonctionnaire'),
                     ('E', 'employé'),
                     ('C', 'commerçant'),
                     ('Y', 'femme au foyer'),
                     ('T', 'étudiant'),
                     ('D', 'cadre'),
                     ('L', 'profession libérale'),
                     ('O', 'au chômage'),
                )
    profession = models.CharField(verbose_name="Profession",
                                  max_length=1,
                                  choices=PROFESSION_CHOICES)

    ASSURANCE_CHOICES = (
                     ('N', 'CNAS'),
                     ('S', 'CASNOS'),
                     ('A', 'Autre'),
                     ('O', 'Non assuré'),
                )
    assurance = models.CharField(verbose_name="Assurance sociale",
                                 max_length=1,
                                 choices=ASSURANCE_CHOICES)
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
    obesity = models.BooleanField("obèse", default=True)
    sedentarity = models.BooleanField("sédentarité", default=True)
    heredity = models.BooleanField("hérédité coronarienne",
                                   default=False)
    history = models.TextField("antécedents")
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

    def slug(self):
        return slugify(self.name, self.birth)
#    def get_absolute_url(self):
#        return reverse('detail_patient', kwargs={'pk': self.pk})
    # def _get_unique_slug(self):
    #     slug = slugify(self.title, self.birth)
    #     unique_slug = slug
    #     num = 1
    #     while Patient.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, num)
    #         num += 1
    #     return unique_slug

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #     super().save()
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
    auscultation = models.CharField(max_length=50, blank=True,
                                    null=True)
    ivg = models.BooleanField(default=False)
    ivd = models.BooleanField(default=False)
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
    rythm = models.CharField(max_length=1, choices=RYTHM_CHOICES)
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
    necrosis = models.CharField(max_length=1, choices=TERRITORY)
    ischaemia = models.CharField(max_length=1, choices=TERRITORY)
    lesion = models.CharField(max_length=1, choices=TERRITORY)
    t_inversion = models.CharField(max_length=1, choices=TERRITORY)
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

