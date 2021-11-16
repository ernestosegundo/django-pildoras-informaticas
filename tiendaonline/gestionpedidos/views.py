from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def buscar_articulos(request):
    return render(request, "buscararticulos.html")

def buscar(request):
    mensaje = "Artículo buscado: %r" %request.GET["articulo"]

    return HttpResponse(mensaje)

