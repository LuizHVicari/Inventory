from django.shortcuts import render
from django.views.generic import TemplateView

class DasahboardView(TemplateView):
  template_name = '_base.html'