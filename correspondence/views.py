from django.shortcuts import render
from .models import Courrier, Arret, Stomato, Certificat
from clinic.models import (Patient)
from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView)
from django.http import HttpResponse
from django.template.loader import get_template  # render_to_string
from subprocess import Popen, PIPE
import tempfile
import os
import operator
from six.moves import reduce
from django.core.files import File

# Create your views here.

def courrier_pdf(request, slug, pk):
    entry = Courrier.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'courrier': entry, 'patient': source})
    template = get_template('correspondence/courrier.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_courrier{entry.courrier_date}_{entry.correspondant}'
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


def certificat_pdf(request, slug, pk):
    entry = Certificat.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'certificat': entry, 'patient': source})
    template = get_template('correspondence/certificat.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_certificat{entry.certificat_date}_{entry.correspondant}'
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


def stomato_pdf(request, slug, pk):
    entry = Stomato.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'stomato': entry, 'patient': source})
    template = get_template('correspondence/stomato.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_stomato{entry.stomato_date}_{entry.dentist}'
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
                ['context', filename, tempdir],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r


def arret_pdf(request, slug, pk):
    entry = Arret.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'arret': entry, 'patient': source})
    template = get_template('correspondence/arret.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_courrier{entry.redaction_date}_{entry.type_arret}'
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
