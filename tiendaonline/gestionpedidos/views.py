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

        articulos = Articulo.objects.filter(nombre__icontains=articulo)

        return render(request, "resultadosbusquedaarticulos.html", {"articulos": articulos, "query": articulo})
    else:
        mensaje = "No se ingresó el artículo a buscar"

    return HttpResponse(mensaje)

