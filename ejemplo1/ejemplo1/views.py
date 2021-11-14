from django.http import HttpResponse
from django.template import Template, Context
import datetime

def curso_django(request):
    return HttpResponse("¡Este es un ejemplo del curso de Django de Píldoras Informáticas!")

def ruta_curso(request):
    return HttpResponse("El curso de Django está disponible en Youtube en el canal de Píldoras Informáticas: https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB")

def fecha(request):
    la_fecha = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    La fecha y hora actual es: %s
    </h2>
    </body>
    </html>""" % la_fecha

    return HttpResponse(documento)

def edad_futura(request, anio):
    edad_actual = 45
    periodo = anio - 2021
    edad_futura = edad_actual + periodo

    documento = "<html><body><h3>En el año %s tendrás %s años</h3></body></html>" %(anio, edad_futura)

    return HttpResponse(documento)

def edad_futura_edad(request, edad, anio):
    periodo = anio - 2021
    edad_futura = edad + periodo

    documento = "<html><body><h3>En el año %s tendrás %s años</h3></body></html>" %(anio, edad_futura)

    return HttpResponse(documento)