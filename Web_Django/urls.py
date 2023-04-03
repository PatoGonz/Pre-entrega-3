"""Web_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Registro_lol.views import index, fun_Crear_campeones, fun_Crear_wards, fun_Crear_mapas, fun_Mostrar_informacion, fun_Busqueda_bd, fun_Busqueda

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('Registro_campeones', fun_Crear_campeones, name="Registro_campeones"),
    path('Registro_wards', fun_Crear_wards, name="Registro_wards"),
    path('Registro_mapas', fun_Crear_mapas, name="Registro_mapas"),
    path('informacion', fun_Mostrar_informacion, name="informacion"),
    path('busquedaCampeon', fun_Busqueda_bd, name="busquedaCampeon"),
    path('busqueda/', fun_Busqueda),
    ]
