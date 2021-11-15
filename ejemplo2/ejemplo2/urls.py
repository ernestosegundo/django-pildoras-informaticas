"""ejemplo2 URL Configuration

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
from ejemplo2.views import ejemplo_plantilla, ejemplo_plantilla_listas, ejemplo_plantilla_variables

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ejemplo-plantilla/', ejemplo_plantilla),
    path('ejemplo-plantilla-variables/', ejemplo_plantilla_variables),
    path('ejemplo-plantilla-listas/', ejemplo_plantilla_listas),
]
