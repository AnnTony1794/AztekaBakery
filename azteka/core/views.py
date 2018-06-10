from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'core/index.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class StoreView(TemplateView):
    template_name = 'core/store.html'


class SampleView(TemplateView):
    template_name = 'core/sample.html'