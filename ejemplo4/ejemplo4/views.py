from django.http import HttpResponse
from django.template.loader import get_template

def get_index(request):
    la_plantilla = get_template("index.html")

    el_documento = la_plantilla.render({"saludo": "Hola", "despedida": "Adios"})

    return HttpResponse(el_documento)