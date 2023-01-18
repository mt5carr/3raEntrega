from django.db import models

# Create your models here.

class Tareas(models.Model):    
    tarea = models.CharField(max_length=254)
    fecha_vencimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.tarea}"


class Proyectos(models.Model):
    proyecto = models.CharField(max_length=64)    
    fecha_inicio = models.DateField(null=True)

    def __str__(self):
        return f"{self.proyecto}"


class Clientes(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_alta = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"