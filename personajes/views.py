from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from personajes.models import Bueno, Neutral, Malo, Total
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
        template_name='personajes/buenos.html',
        context={},
    )
    return respuesta_http

def sel_neutrales (request):
    respuesta_http= render(
        request=request,
        template_name='personajes/neutrales.html',
        context={},
    )
    return respuesta_http

def sel_malos (request):
    respuesta_http= render(
        request=request,
        template_name='personajes/malos.html',
        context={},
    )
    return respuesta_http

# VISTAS DE LISTAR
def listar_buenos(request):
    contexto = {
        "per_buenos": Bueno.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='personajes/buenos.html',
        context=contexto,
    )
    return http_response

def listar_neutrales(request):
    contexto = {
        "per_neutrales": Neutral.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='personajes/neutrales.html',
        context=contexto,
    )
    return http_response

def listar_malos(request):
    contexto = {
        "per_malos": Malo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='personajes/malos.html',
        context=contexto,
    )
    return http_response

#VISTAS DE BUSCAR
class BuenoDetailView(DetailView):
    model = Bueno
    success_url = reverse_lazy('lista_buenos')

class NeutralDetailView(DetailView):
    model = Neutral
    success_url = reverse_lazy('lista_neutrales')
  
class MaloDetailView(DetailView):
    model = Malo
    success_url = reverse_lazy('lista_malos')
 



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
            entotal = Total(nombre=nombre, sexo=sexo, bio=bio, naturaleza='Bueno')
            entotal.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_buenos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = BuenoFormulario()
    http_response = render(
        request=request,
        template_name='personajes/formulario_bueno.html',
        context={'formulario': formulario}
    )
    return http_response

class NeutralCreateView(CreateView):
    model = Neutral
    fields = ('nombre', 'sexo', 'bio')
    success_url = reverse_lazy('lista_neutrales')
    model = Total
    neutral = 'Neutral'
    fields = ('nombre', 'sexo', 'bio', 'neutral')

class MaloCreateView(CreateView):
    model = Malo
    fields = ('nombre', 'sexo', 'bio')
    success_url = reverse_lazy('lista_malos')
    model = Total
    malo = 'Malo'
    fields = ('nombre', 'sexo', 'bio', 'malo')

#URLS DE ELIMINAR ENTRADA
class BuenoDeleteView(DeleteView):
    model = Bueno
    model = Total
    success_url = reverse_lazy('lista_buenos')

class NeutralDeleteView(DeleteView):
    model = Neutral
    model = Total
    success_url = reverse_lazy('lista_neutrales')

class MaloDeleteView(DeleteView):
    model = Malo
    model = Total
    success_url = reverse_lazy('lista_malos')
