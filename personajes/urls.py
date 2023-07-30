from django.contrib import admin
from django.urls import path
from personajes.views import seleccionar, sel_buenos, sel_neutrales, sel_malos
from personajes.views import listar_buenos, listar_neutrales, listar_malos
from personajes.views import BuenoDetailView, NeutralDetailView, MaloDetailView
from personajes.views import crear_bueno, NeutralCreateView, MaloCreateView
from personajes.views import BuenoDeleteView, NeutralDeleteView, MaloDeleteView

urlpatterns = [
    #URLS iniciales y navbar
    path('seleccion/', seleccionar, name='seleccion'),
    path('buenos/', sel_buenos, name='buenos'),    
    path('neutrales', sel_neutrales, name='neutrales'),
    path('malos/', sel_malos, name='malos'),

    #URLS de listar
    path('todos-buenos/', listar_buenos, name='lista_buenos'),
    path('todos-neutrales/', listar_neutrales, name='lista_neutrales'),
    path('todos-malos/', listar_malos, name='lista_malos'),

    #URLS de busqueda
    path('busqueda-bueno/<int:pk>/', BuenoDetailView.as_view(), name="busqueda_bueno"),
    path('busqueda-neutral/<int:pk>/', NeutralDetailView.as_view(), name="busqueda_neutral"),
    path('busqueda-malo/<int:pk>/', MaloDetailView.as_view(), name="busqueda_malo"),

    #URLS de crear entrada
    path('crear-bueno/', crear_bueno, name="bueno_creado"),
    path('crear-neutral/', NeutralCreateView.as_view(), name="neutral_creado"),
    path('crear-malo/', MaloCreateView.as_view(), name="malo_creado"),

    #URLS de eliminar entrada
    path('eliminar-bueno/<int:pk>/', BuenoDeleteView.as_view(), name="bueno_eliminado"),
    path('eliminar-neutral/<int:pk>/', NeutralDeleteView.as_view(), name="neutral_eliminado"),
    path('eliminar-malo/<int:pk>/', MaloDeleteView.as_view(), name="malo_eliminado"),
]