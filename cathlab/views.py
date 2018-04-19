from django.shortcuts import render
from .models import Coronarographie, Coroscan
from clinic.models import (Patient)
from django.views.generic import (ListView, DetailView, TemplateView,
                                  CreateView, UpdateView)
from django.http import HttpResponse
from django.template.loader import get_template  # render_to_string
from subprocess import Popen, PIPE
import tempfile
import os

# Create your views here.

def coronarographie_pdf(request, slug, pk):
    entry = Coronarographie.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'coronarographie': entry, 'patient': source})
    template = get_template('cathlab/coro.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_coro{entry.intervention_date}'
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
                ['context', filename, '--purgeall'],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r


def coroscan_pdf(request, slug, pk):
    entry = Coroscan.objects.get(pk=pk)
    source = Patient.objects.get(slug=slug)
#    context = Context({ 'consultation': entry, 'patient': source })
    context = dict({'coroscan': entry, 'patient': source})
    template = get_template('cathlab/coroscan.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # save the file to disk
    filename = f'{entry.patient}_coroscan{entry.coroscan_date}'
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
                ['context', filename, '--purgeall'],
                stdin=PIPE,
                stdout=PIPE,)
        process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, f'{filename}.pdf'), 'rb') as f:
            pdf = f.read()
            r = HttpResponse(content_type='application/pdf')
            r.write(pdf)
            return r

