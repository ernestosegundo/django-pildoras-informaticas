"""ejemplo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo1.views import curso_django, edad_futura, edad_futura_edad, ruta_curso, fecha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso-django/', curso_django),
    path('ruta-curso/', ruta_curso),
    path('fecha-actual/', fecha),
    path('edad-futura/<int:anio>', edad_futura),
    path('edad-futura/<int:edad>/<int:anio>', edad_futura_edad)
]
