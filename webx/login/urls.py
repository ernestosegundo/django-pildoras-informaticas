from django.urls import path

from .views import Registro

urlpatterns = [
    path('', Registro.as_view(), name="Login"),
]