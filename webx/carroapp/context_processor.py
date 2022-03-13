from .carro import Carro

def importe_total_carro(request):
    carro = Carro(request)

    total = 0
    
    #if request.user.is_authenticated:
    for key, value in request.session["carro"].items():
        total += float(value["precio"])

    return {"importe_total_carro": total}