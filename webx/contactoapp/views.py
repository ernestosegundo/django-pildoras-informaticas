from django.shortcuts import render, redirect

from django.core.mail import EmailMessage

from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde app Django", 
                    "El usuario con nombre {} con el correo {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido),
                    "", ["rsernesto@outloook.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
                
    return render(request, "contacto/contacto.html", {"formulario_contacto": formulario_contacto})