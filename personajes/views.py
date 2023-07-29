from django.shortcuts import render

# Create your views here.

def iniciar_website (request):
    respuesta_http= render(
        request=request,
        template_name='first_html.html',
        context={},
    )
    return respuesta_http