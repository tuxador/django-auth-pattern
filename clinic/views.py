from django.shortcuts import render
from .models import Patient, Consultation, Stress
from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView)
from django.http import HttpResponse
from django.template.loader import get_template  # render_to_string
from subprocess import Popen, PIPE
import tempfile
import os
import operator
from django.db.models import Q
from six.moves import reduce
from django.core.files import File
import uuid
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
#        context['admissions'] = Admission.objects.filter(patient=self.object)
        context['consultations'] = Consultation.objects.filter(patient=self.object)
#        context['ordonnances'] = Ordonnance.objects.filter(patient=self.object)
#        context['certificats'] = Certificat.objects.filter(patient=self.object)
#        context['arrets'] = Arret.objects.filter(patient=self.object)
#        context['biologies'] = Biology.objects.filter(patient=self.object)
#        context['coronarographies'] = Coronarographie.objects.filter(patient=self.object)
 #       context['stimulations'] = Stimulation.objects.filter(patient=self.object)
        return context



def consultation_pdf(request, slug, pk):
    entry = Consultation.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
    #    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'consultation': entry, 'patient': source})
    template = get_template('clinic/consultation.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = uuid.uuid4()
    # Python3 only. For python2 check out the docs!
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, str(filename))
        with open(filename, 'wb') as infile:
            infile.write(rendered_tpl)
###########################################################
# from django.core.files import File
#      with open('/tmp/hello.world', 'w') as f:
#...     myfile = File(f)
#...     myfile.write('Hello World')
#####################################################
        process = Popen(
                ['context', filename, tempdir],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r
