from django.shortcuts import render
from django.http import HttpResponse
from Registro_lol.models import Crear_campeones, Crear_ward, Crear_mapa
from django.urls import reverse_lazy
from Registro_lol.forms import Crear_campeon_form, Crear_ward_form, Crear_mapa_form
# Create your views here.

def index(request):
	return render(request, "Registro_lol/index.html")

def fun_Crear_campeones(request):
 
      if request.method == "POST":
 
            miFormulario = Crear_campeon_form(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  
                  crear_campeon = Crear_campeones(nombre_campeon=informacion["nombre_campeon"], dificultad_campeon=informacion["dificultad_campeon"],descripcion_campeon=informacion["descripcion_campeon"])
                  crear_campeon.save()
                  
                  # OJO: El dejar esta ruta del request vacía da como error el PermisionsDennied.
                  return render(request, 'Registro_lol/Registro_campeones.html')
      else:
            miFormulario = Crear_campeon_form()
 
      return render(request, "Registro_lol/Registro_campeones.html", {"miFormulario": miFormulario})

def fun_Crear_wards(request):
 
      if request.method == "POST":
 
            miFormulario = Crear_ward_form(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  
                  crear_ward = Crear_ward(nombre_ward=informacion["nombre_ward"], rango_vision=informacion["rango_vision"],descripcion_ward=informacion["descripcion_ward"])
                  crear_ward.save()

                  # OJO: El dejar esta ruta del request vacía da como error el PermisionsDennied.
                  return render(request, 'Registro_lol/Registro_wards.html')
      else:
            miFormulario = Crear_ward_form()
 
      return render(request, "Registro_lol/Registro_wards.html", {"miFormulario": miFormulario})

def fun_Crear_mapas(request):
 
      if request.method == "POST":
 
            miFormulario = Crear_mapa_form(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  
                  crear_campeon = Crear_mapa(nombre_mapa=informacion["nombre_mapa"], cantidad_jugadores=informacion["cantidad_jugadores"],descripcion_mapa=informacion["descripcion_mapa"])
                  crear_campeon.save()

                  # OJO: El dejar esta ruta del request vacía da como error el PermisionsDennied.
                  return render(request, 'Registro_lol/Registro_mapas.html')
      else:
            miFormulario = Crear_mapa_form()
 
      return render(request, "Registro_lol/Registro_mapas.html", {"miFormulario": miFormulario})