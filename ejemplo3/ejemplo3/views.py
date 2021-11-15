from django.http import HttpResponse
from django.template import Template, Context
import random

def get_numero(request):
    documento_plantilla = open("D:/DjangoProjects/ejemplo3/ejemplo3/plantillas/numeroaleatorio.html")

    el_numero = round(random.random()*100)

    la_plantilla = Template(documento_plantilla.read())

    documento_plantilla.close()

    el_contexto = Context({"numero_aleatorio": el_numero})

    documento = la_plantilla.render(el_contexto)

    return HttpResponse(documento)

def get_frase(request):
    documento_plantilla = open("D:/DjangoProjects/ejemplo3/ejemplo3/plantillas/frasealeatoria.html")

    la_canasta = ""

    las_frutas = ["naranja", "fresa", "pera", "manzana", "durazno", "mandarina", "uva", "banana", "papaya", "ciruelo"]

    for x in range(3):
        la_canasta += " " + random.choice(las_frutas)

    la_plantilla = Template(documento_plantilla.read())

    documento_plantilla.close()

    el_contexto = Context({"frase_aleatoria": la_canasta,
                           "frutas": las_frutas})

    documento = la_plantilla.render(el_contexto)

    return HttpResponse(documento)
