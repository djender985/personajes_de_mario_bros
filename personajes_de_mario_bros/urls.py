from django.contrib import admin
from django.urls import path, include
from personajes_de_mario_bros.views import dar_bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dar_bienvenida, name="inicio"),
    path('naturaleza/', include("personajes.urls")),
]
