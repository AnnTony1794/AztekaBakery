from django.shortcuts import render
from django.views.generic import ListView
from .models import Service

# Create your views here.


class ServicesView(ListView):
    model = Service
    template_name = 'services/services.html'
    paginate_by = 10
    context_object_name = 'services_list'