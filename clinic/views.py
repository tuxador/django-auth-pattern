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

# Create your views here.
class ListPatients(ListView):
    model = Patient
    context_object_name = 'patients'

