from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render
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
        return render(request, "trabajando.html")

    return render(request, "contacto.html")