from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import message, send_mail
from django.conf import settings

from gestionpedidos.models import Articulo

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
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["rsernesto@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "realizado.html", {"realizado": "El mensaje de correo electrónico se envió correctamente. En breve le contactaremos a " + request.POST["email"]})

    return render(request, "contacto.html")