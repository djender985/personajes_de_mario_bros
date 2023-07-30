from django.contrib import admin
from django.urls import path
from personajes.views import (
    seleccionar, sel_buenos, sel_neutrales, sel_malos,
    listar_buenos, listar_neutrales, listar_malos,
    buscar_bueno, buscar_neutral, buscar_malo,
    crear_bueno, crear_neutral, crear_malo,
    borrar_bueno, borrar_neutral, borrar_malo
)
urlpatterns = [
    #URLS iniciales y navbar
    path('seleccion/', seleccionar, name='seleccion'),
    
    #URLS de listar
    path('lista-buenos/', listar_buenos, name='lista_buenos'),
    path('lista-neutrales/', listar_neutrales, name='lista_neutrales'),
    path('lista-malos/', listar_malos, name='lista_malos'),

    #URLS de crear entrada
    path('crear-bueno/', crear_bueno, name="crear_bueno"),
    path('crear-neutral/', crear_neutral, name="crear_neutral"),
    path('crear-malo/', crear_malo, name="crear_malo"),

    #URLS de busqueda
    path('buscar-bueno/', buscar_bueno, name="buscar_bueno"),
    path('buscar-neutral/', buscar_neutral, name="buscar_neutral"),
    path('buscar-malo/', buscar_malo, name="buscar_malo"),

    #URLS de eliminar entrada
    path('borrar-bueno', borrar_bueno, name="borrar_bueno"),
    path('borrar-neutral', borrar_neutral, name="borrar_neutral"),
    path('borrar-malo', borrar_malo, name="borrar_malo"),
]