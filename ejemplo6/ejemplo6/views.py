from django.shortcuts import render

def get_index(request):
    return render(request, "index.html", {"nombre": "Ernesto Segundo", "ciudad": "Moyobamba", "secciones": ["Institucional", "Transparencia", "Convocatorias", "Publicaciones", "Servicios"]})

def get_services(request):
    return render(request, "servicios.html", {"nombre": "Ernesto Segundo", "ciudad": "Moyobamba", "secciones": ["Institucional", "Transparencia", "Convocatorias", "Publicaciones", "Servicios"], "servicios": ["Registro de visitas", "SIGA WEB", "Correo institucional", "Intranet", "Reportes"]})