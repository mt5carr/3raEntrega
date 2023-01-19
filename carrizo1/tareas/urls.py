from django.urls import path
from tareas.views import (
    listar_tareas, 
    crear_tarea, 
    buscar_tarea,
    listar_proyectos,
    crear_proyecto, 
    buscar_proyecto,
    listar_clientes, 
    crear_cliente,
    buscar_cliente,
    sobre_mi, 
    inicio
)

urlpatterns = [
    path("lista-tareas/", listar_tareas, name="lista_tareas"),
    path("lista-proyectos/", listar_proyectos, name="lista_proyectos"),
    path("lista-clientes/", listar_clientes, name="lista_clientes"), 
    path("sobre-mi/", sobre_mi, name="sobre_mi"),
    path("/", inicio, name="inicio"),
    path("crear-tarea", crear_tarea, name="crear_tarea"),
    path("crear-proyecto", crear_proyecto, name="crear_proyecto"),
    path("crear-cliente", crear_cliente, name="crear_cliente"),
    path("buscar-tarea", buscar_tarea, name="buscar_tarea"),
    path("buscar-proyecto", buscar_proyecto, name="buscar_proyecto"),
    path("buscar-cliente", buscar_cliente, name="buscar_cliente")
]
