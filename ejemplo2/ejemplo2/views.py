from django.http import HttpResponse
from django.template import Template, Context

class Estudiante(object):
    def __init__(self, nombre, apellido):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido

def ejemplo_plantilla(request):
    documento_externo = open("D:/DjangoProjects/ejemplo2/ejemplo2/plantillas/plantillaejemplo.html")

    plt = Template(documento_externo.read())

    documento_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def ejemplo_plantilla_variables(request):
    documento_externo = open("D:/DjangoProjects/ejemplo2/ejemplo2/plantillas/plantillaejemplovariables.html")

    nombre = "Juan"

    apellido = "Díaz"

    alumno = Estudiante("Ernesto Segundo", "Ríos Sandoval")
    
    plt = Template(documento_externo.read())

    documento_externo.close()

    ctx = Context({"nombre_persona": nombre, 
            "apellido_persona": apellido, 
            "url_curso": "https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB",
            "estudiante": alumno.nombre + " " + alumno.apellido})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def ejemplo_plantilla_listas(request):
    documento_externo = open("D:/DjangoProjects/ejemplo2/ejemplo2/plantillas/plantillaejemplolistas.html")

    plt = Template(documento_externo.read())

    documento_externo.close()

    ctx = Context({"secciones": ["Institucional", "Transparencia", "Convocatorias", "Publicaciones", "Servicios"],
                "colores": ["rojo", "verde", "blanco"]})

    documento = plt.render(ctx)

    return HttpResponse(documento)
