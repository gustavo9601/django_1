from django.contrib import admin

# Register your models here.
from personas.models import Persona, Domicilio

# Regustro de modelos para que aparescan en la consola
admin.site.register(Persona)
admin.site.register(Domicilio)