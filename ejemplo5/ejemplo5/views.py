from django.shortcuts import render

def get_index(request):
    return render(request, "index.html", {"nombre": "Ernesto Segundo", "ciudad": "Moyobamba", "secciones": ["Institucional", "Transparencia", "Convocatorias", "Publicaciones", "Servicios"]})    