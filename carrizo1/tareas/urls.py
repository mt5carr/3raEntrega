from django.urls import path
from tareas.views import (
    listar_tareas, 
    crear_tarea, 
    listar_proyectos,
    crear_proyecto, 
    listar_clientes, 
    crear_cliente,
    sobre_mi, 
    inicio
)

urlpatterns = [
    path("lista-tareas/", listar_tareas, name="lista_tareas"),
    path("lista-proyectos/", listar_proyectos, name="lista_proyectos"),
    path("lista-clientes/", listar_clientes, name="lista_clientes"), 
    path("sobre-mi/", sobre_mi, name="sobre_mi"),
    path("inicio/", inicio, name="inicio"),
    path("crear-tarea", crear_tarea, name="crear_tarea"),
    path("crear-proyecto", crear_proyecto, name="crear_proyecto"),
    path("crear-cliente", crear_cliente, name="crear_cliente")
]
