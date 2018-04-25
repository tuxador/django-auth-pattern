from django.shortcuts import render
from .models import Patient, Consultation, Stress, Admission, FicheTechnique
from correspondence.models import (Ordonnance, Courrier, Certificat,
                                   Arret, Stomato)
from cathlab.models import Coronarographie, Coroscan
from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView)
from django.http import HttpResponse
from django.template.loader import get_template  # render_to_string
from subprocess import Popen, PIPE
import tempfile
import os
from authtest.settings import BASE_DIR
import operator
from django.db.models import Q
from six.moves import reduce
from django.core.files import File
# Create your views here.


class ListPatients(ListView):
    model = Patient
    context_object_name = 'patients'


class PatientSearchListView(ListPatients):
    """
    Display the patient List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(PatientSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(phone__icontains=q) for q in query_list))
                # reduce(operator.and_,
                # (Q(tags__icontains=q) for q in query_list))
            )

        return result


class DetailPatient(DetailView):
    model = Patient
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailPatient, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['admissions'] = Admission.objects.filter(patient=self.object)
        context['consultations'] = Consultation.objects.filter(patient=self.object)
        context['fiches'] = FicheTechnique.objects.filter(patient=self.object)
        context['stresss'] = Stress.objects.filter(patient=self.object)
        context['ordonnances'] = Ordonnance.objects.filter(patient=self.object)
        context['courriers'] = Courrier.objects.filter(patient=self.object)
        context['certificats'] = Certificat.objects.filter(patient=self.object)
        context['arrets'] = Arret.objects.filter(patient=self.object)
        context['stomatos'] = Stomato.objects.filter(patient=self.object)
        context['coroscans'] = Coroscan.objects.filter(patient=self.object)
        context['coronarographies'] = Coronarographie.objects.filter(patient=self.object)
#       context['stimulations'] = Stimulation.objects.filter(patient=self.object)
        return context


class ListAdmissions(ListView):
    model = Admission
    context_object_name = 'admissions'


class CurrentAdmissions(ListView):
    model = Admission
    context_object_name = 'admissions'
    template_name = 'clinic/admission_current.html'

    def get_queryset(self):
        return Admission.objects.filter(sortant=False)


# CreateViews


class CreatePatient(CreateView):
    model = Patient
    fields = "__all__"
    success_url = 'clinique/patients'


class UpdatePatient(UpdateView):
    model = Patient
    fields = '__all__'
#    group_required = u'Cardiologues'
#    form = PatientForm
#    success_url = reverse_lazy('detail_patient')
    success_url = 'clinique/patients'


class CreateConsultation(CreateView):
    model = Consultation
    fields = "__all__"
    success_url = 'clinique/patients'


class UpdateConsultation(UpdateView):
    model = Consultation
    fields = "__all__"
    success_url = 'clinique/patients'


class CreateAdmission(CreateView):
    model = Admission
    fields = "__all__"
    success_url = 'clinique/patients'


class UpdateAdmission(UpdateView):
    model = Admission
    fields = '__all__'
#    group_required = u'Cardiologues'
#    form = PatientForm
    success_url = 'clinique/patients'


class CreateFicheTechnique(CreateView):
    model = FicheTechnique
    fields = "__all__"
    success_url = '/'


class UpdateFicheTechnique(UpdateView):
    model = FicheTechnique
    fields = "__all__"
    success_url = '/'


class CreateStress(CreateView):
    model = Stress
    fields = "__all__"
    success_url = 'clinique/patients'


class UpdateStress(UpdateView):
    model = Stress
    fields = "__all__"
    success_url = 'clinique/patients'


def consultation_pdf(request, slug, pk):
    entry = Consultation.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'consultation': entry, 'patient': source})
    template = get_template('clinic/consultation.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_consultation{entry.consultation_date}'
    # Python3 only. For python2 check out the docs!
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, str(filename))
        with open(filename, 'wb') as infile:
            infile.write(rendered_tpl)
###########################################################
# from django.core.files import File
#      with open('/tmp/hello.world', 'w') as f:
# ..     myfile = File(f)
# ..     myfile.write('Hello World')
#####################################################
        process = Popen(
                ['context', filename, '--purgeall'],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(BASE_DIR, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r


def admission_pdf(request, slug, pk):
    entry = Admission.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'admission': entry, 'patient': source})
    template = get_template('clinic/admission.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_admission{entry.admission_date}'
    # Python3 only. For python2 check out the docs!
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, str(filename))
        with open(filename, 'wb') as infile:
            infile.write(rendered_tpl)
###########################################################
# from django.core.files import File
#      with open('/tmp/hello.world', 'w') as f:
# ..     myfile = File(f)
# ..     myfile.write('Hello World')
#####################################################
        process = Popen(
                ['context', filename, '--purgeall'],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r


def stress_pdf(request, slug, pk):
    entry = Stress.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'stress': entry, 'patient': source})
    template = get_template('clinic/stress.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_stress{entry.stress_date}'
    # Python3 only. For python2 check out the docs!
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, str(filename))
        with open(filename, 'wb') as infile:
            infile.write(rendered_tpl)
###########################################################
# from django.core.files import File
#      with open('/tmp/hello.world', 'w') as f:
# ..     myfile = File(f)
# ..     myfile.write('Hello World')
#####################################################
        process = Popen(
                ['context', filename, '--purgeall'],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r


def fiche_pdf(request, slug, pk):
    entry = FicheTechnique.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'fiche': entry, 'patient': source})
    template = get_template('clinic/fiche_technique.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_fiche{entry.date_fiche}'
    # Python3 only. For python2 check out the docs!
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, str(filename))
        with open(filename, 'wb') as infile:
            infile.write(rendered_tpl)
###########################################################
# from django.core.files import File
#      with open('/tmp/hello.world', 'w') as f:
#          myfile = File(f)
#          myfile.write('Hello World')
#####################################################
        process = Popen(
                ['context', filename, '--purgeall'],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r
