from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from personajes.models import Bueno, Neutral, Malo
from personajes.forms import BuenoFormulario, NeutralFormulario, MaloFormulario


# VISTAS INICIALES
def seleccionar (request):
    respuesta_http= render(
        request=request,
        template_name='personajes/seleccion.html',
        context={},
    )
    return respuesta_http

def sel_buenos (request):
    respuesta_http= render(
        request=request,
        template_name='personajes/lista_buenos.html',
        context={},
    )
    return respuesta_http

def sel_neutrales (request):
    respuesta_http= render(
        request=request,
        template_name='personajes/lista_neutrales.html',
        context={},
    )
    return respuesta_http

def sel_malos (request):
    respuesta_http= render(
        request=request,
        template_name='personajes/lista_malos.html',
        context={},
    )
    return respuesta_http

# VISTAS DE LISTAR
def listar_buenos(request):
    contexto = {
        "buenos": Bueno.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='personajes/lista_buenos.html',
        context=contexto,
    )
    return http_response

def listar_neutrales(request):
    contexto = {
        "neutrales": Neutral.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='personajes/lista_neutrales.html',
        context=contexto,
    )
    return http_response

def listar_malos(request):
    contexto = {
        "malos": Malo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='personajes/lista_malos.html',
        context=contexto,
    )
    return http_response

#VISTAS DE BUSCAR
def buscar_bueno(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        bueno = Bueno.objects.filter(nombre__contains=busqueda)        
        contexto = {
            "buenos": bueno,
        }
        http_response = render(
            request=request,
            template_name='personajes/lista_buenos.html',
            context=contexto,
        )
        return http_response

def buscar_neutral(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        neutral = Neutral.objects.filter(nombre__contains=busqueda)        
        contexto = {
            "neutrales": neutral,
        }
        http_response = render(
            request=request,
            template_name='personajes/lista_neutrales.html',
            context=contexto,
        )
        return http_response

def buscar_malo(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        malo = Malo.objects.filter(nombre__contains=busqueda)        
        contexto = {
            "malos": malo,
        }
        http_response = render(
            request=request,
            template_name='personajes/lista_malos.html',
            context=contexto,
        )
        return http_response

#VISTAS DE CREAR ENTRADAS
def crear_bueno(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = BuenoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            sexo = data["sexo"]
            bio = data["bio"]
            # creo un curso en memoria RAM
            bueno = Bueno(nombre=nombre, sexo=sexo, bio=bio)
            # Lo guardan en la Base de datos
            bueno.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_buenos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = BuenoFormulario()
    http_response = render(
        request=request,
        template_name='personajes/formulario_buenos.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_neutral(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = NeutralFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            sexo = data["sexo"]
            bio = data["bio"]
            # creo un curso en memoria RAM
            neutral = Neutral(nombre=nombre, sexo=sexo, bio=bio)
            # Lo guardan en la Base de datos
            neutral.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_neutrales')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = BuenoFormulario()
    http_response = render(
        request=request,
        template_name='personajes/formulario_neutrales.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_malo(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = MaloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            sexo = data["sexo"]
            bio = data["bio"]
            # creo un curso en memoria RAM
            malo = Malo(nombre=nombre, sexo=sexo, bio=bio)
            # Lo guardan en la Base de datos
            malo.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_malos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = MaloFormulario()
    http_response = render(
        request=request,
        template_name='personajes/formulario_malos.html',
        context={'formulario': formulario}
    )
    return http_response

#VISTAS DE ELIMINAR ENTRADA
def borrar_bueno(request, id):
    # obtienes el curso de la base de datos
    bueno = Bueno.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        bueno.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_buenos')
        return redirect(url_exitosa)


def borrar_neutral(request, id):
    # obtienes el curso de la base de datos
    neutral = Neutral.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        neutral.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_neutrales')
        return redirect(url_exitosa)

def borrar_malo(request, id):
    # obtienes el curso de la base de datos
    malo = Malo.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        malo.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_malos')
        return redirect(url_exitosa)
