from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def dar_bienvenida (request):
    respuesta_http= render(
        request=request,
        template_name='base.html',
        context={},
    )
    return respuesta_http
