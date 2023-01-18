from django.contrib import admin
from tareas.models import Tareas, Proyectos, Clientes
# Register your models here.

admin.site.register(Tareas)
admin.site.register(Proyectos)
admin.site.register(Clientes)