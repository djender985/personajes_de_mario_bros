from django.contrib import admin
from django.urls import path, include
from personajes.views import iniciar_website

urlpatterns = [
    path('principal/', iniciar_website),
]