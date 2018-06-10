from django.shortcuts import render
from django.views.generic import ListView
from .models import Service

# Create your views here.


class ServicesView(ListView):
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services_list'
    paginate_by = 5