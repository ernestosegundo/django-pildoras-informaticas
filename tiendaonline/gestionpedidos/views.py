from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import message, send_mail
from django.conf import settings

from gestionpedidos.models import Articulo
from gestionpedidos.forms import FormularioContacto

# Create your views here.
def buscar_articulos(request):
    return render(request, "buscararticulos.html")

def buscar(request):
    if request.GET["articulo"]:
        mensaje = "Artículo buscado: %r" %request.GET["articulo"]

        articulo = request.GET["articulo"]

        if len(articulo) > 30:
            mensaje = "Texto de búsqueda demasiado largo"
        else:
            articulos = Articulo.objects.filter(nombre__icontains=articulo)

            return render(request, "resultadosbusquedaarticulos.html", {"articulos": articulos, "query": articulo})
    else:
        mensaje = "No se ingresó el artículo a buscar"

    return HttpResponse(mensaje)

def contacto(request):
    if request.method == "POST":
        formulario_contacto = FormularioContacto(request.POST)

        if formulario_contacto.is_valid():
            datos_formulario_contacto = formulario_contacto.cleaned_data

            send_mail(datos_formulario_contacto["asunto"], 
                    datos_formulario_contacto["mensaje"], 
                    datos_formulario_contacto.get("email", ""), ["rsernesto@gmail.com"],)    

            return render(request, "realizado.html", {"realizado": "El mensaje de correo electrónico se envió correctamente. En breve le contactaremos a " + request.POST["email"]})
    else:
        formulario_contacto = FormularioContacto()

    return render(request, "formulariocontacto.html", {"form": formulario_contacto})    

 