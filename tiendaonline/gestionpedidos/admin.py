from django.contrib import admin
from gestionpedidos.models import Cliente, Articulo, Pedido

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    search_fields = ("nombre", "seccion")

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    search_fields = ("numero", "fecha")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidoAdmin)