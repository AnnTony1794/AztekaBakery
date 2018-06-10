from django.contrib import admin
from .models import Service
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # Sirve para ver las columnas en el CRUD del administrador
    # Recibe de valor una tupla con los valores que queremos mostrar
    list_display = ('title',)
    # ordering es para ordenar y también recibe una tubla
    # Sirve para poner un buscador en el admin
    search_fields = ('title',)

admin.site.register(Service, ServiceAdmin)