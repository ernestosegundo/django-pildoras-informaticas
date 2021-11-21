from django.shortcuts import render, HttpResponse

from serviciosapp.models import Servicio

# Create your views here.
def home(request):
    return render(request, "webxapp/home.html")

def servicios(request):
    servicios = Servicio.objects.all()

    return render(request, "webxapp/servicios.html", {"servicios": servicios})

def tienda(request):
    return render(request, "webxapp/tienda.html")

def blog(request):
    return render(request, "webxapp/blog.html")

def contacto(request):
    return render(request, "webxapp/contacto.html")