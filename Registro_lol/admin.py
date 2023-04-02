from django.contrib import admin
from Registro_lol.models import Crear_campeones,Crear_ward, Crear_mapa
# Register your models here.

admin.site.register(Crear_campeones),
admin.site.register(Crear_ward),
admin.site.register(Crear_mapa)