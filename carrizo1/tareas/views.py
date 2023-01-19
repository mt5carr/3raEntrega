from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from tareas.models import Tareas, Proyectos, Clientes
from django.db.models import Q


def saludar(request):
    return HttpResponse('Hola Matias')

def listar_tareas(request):
    contexto = {
        'tareas': Tareas.objects.all()
    }
    return render(
        request=request, 
        template_name='tareas/lista_tareas.html',
        context=contexto
    )

def listar_proyectos(request):
    contexto = {
        'proyectos': Proyectos.objects.all()
    }
    return render(
        request=request, 
        template_name='tareas/lista_proyectos.html',
        context=contexto
        )

def listar_clientes(request):
    contexto = {
        'clientes': Clientes.objects.all()
    }
    return render(
        request=request, 
        template_name='tareas/lista_clientes.html',
        context=contexto
        )

def sobre_mi(request):
    return render(request=request, template_name='tareas/sobre_mi.html')
    
def inicio(request):
    return render(request=request, template_name='tareas/inicio.html')

def crear_tarea(request):
    if request.method == "POST":
        data = request.POST
        nueva_tarea = Tareas(tarea=data['tarea'], fecha_vencimiento = data['fecha'])
        nueva_tarea.save()
        return redirect(reverse('lista_tareas')) 
    else:
        return render(
            request=request,
            template_name='tareas/cargar_tarea.html'
            )


def crear_proyecto(request):
    if request.method == "POST":
        data = request.POST
        nuevo_proyecto = Proyectos(proyecto=data['proyecto'], fecha_inicio = data['fecha'])
        nuevo_proyecto.save()
        return redirect(reverse('lista_proyectos')) 
    else:
        return render(
            request=request,
            template_name='tareas/cargar_proyecto.html'
            )

def crear_cliente(request):
    if request.method == "POST":
        data = request.POST
        nuevo_cliente = Clientes(nombre=data['nombre'], apellido=data['apellido'], fecha_alta = data['fecha'])
        nuevo_cliente.save()
        return redirect(reverse('lista_clientes')) 
    else:
        return render(
            request=request,
            template_name='tareas/cargar_cliente.html'
            )


def buscar_tarea(request):
    if request.method == "POST":
        data = request.POST
        tarea_buscada = Tareas.objects.filter(tarea__contains=data['tarea'])       
        contexto = {
            'tareas': tarea_buscada
            }
        return render(
            request=request, 
            template_name='tareas/lista_tareas.html',
            context=contexto
            )

def buscar_proyecto(request):
    if request.method == "POST":
        data = request.POST
        proyecto_buscado = Proyectos.objects.filter(proyecto__contains=data['proyecto'])       
        contexto = {
            'proyectos': proyecto_buscado
            }
        return render(
            request=request, 
            template_name='tareas/lista_proyectos.html',
            context=contexto
            )

def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        cliente_buscado = Clientes.objects.filter(
            Q(nombre__contains=data['cliente']) | Q(apellido__contains=data['cliente'])
            )       
        contexto = {
            'clientes': cliente_buscado
            }
        return render(
            request=request, 
            template_name='tareas/lista_clientes.html',
            context=contexto
            )
