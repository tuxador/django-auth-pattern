from django.forms import ModelForm
from .models import Patient
from django.utils.text import slugify


class PatientForm(ModelForm):

    class Meta:
        model = Patient
        exclude = ('slug',)

        def save(self):
            instance = super(PatientForm, self).save(commit=False)
            instance.slug = slugify(instance.name, instance.birth)
            instance.save()

            return instance
#       instance.slug = slugify(instance.name,instance.birth)
#       super().save()
