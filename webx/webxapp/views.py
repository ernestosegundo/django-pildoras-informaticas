from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "webxapp/home.html")

def tienda(request):
    return render(request, "webxapp/tienda.html")

def blog(request):
    return render(request, "webxapp/blog.html")

def contacto(request):
    return render(request, "webxapp/contacto.html")