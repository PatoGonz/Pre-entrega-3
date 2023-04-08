from django.shortcuts import render
from django.http import HttpResponse
from Registro_lol.models import Crear_campeones, Crear_ward, Crear_mapa
from Registro_lol.forms import Crear_campeon_form, Crear_ward_form, Crear_mapa_form, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
	return render(request, "Registro_lol/index.html")

def fun_Mostrar_informacion(request):

    campeones = Crear_campeones.objects.all()
    total_campeones = len(campeones)

    wards = Crear_ward.objects.all()
    total_wards = len(wards)

    mapas = Crear_mapa.objects.all()
    total_mapas = len(mapas)

    context = {
        "campeones": campeones,
        "total_campeones": total_campeones,
        "wards": wards,
        "total_wards": total_wards,
        "mapas": mapas,
        "total_mapas": total_mapas,
    }
    return render(request, "Registro_lol/informacion.html", context)

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

def fun_Busqueda_bd(request):
      return render(request, "Registro_lol/busquedaCampeon.html")

def fun_Busqueda(LoginRequiredMixin,request):

      if request.GET["nombre_campeon"]:

            nombre_campeon = request.GET["nombre_campeon"]
            campeones = Crear_campeones.objects.filter(nombre_campeon__icontains=nombre_campeon)

            return render(request, "Registro_lol/resultadoBusqueda.html", {"campeones" : campeones, "nombre_campeon":nombre_campeon})
      
      else:

            respuesta = "No enviaste datos."


      return HttpResponse(respuesta)


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "Registro_lol/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "Registro_lol/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "Registro_lol/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Registro_lol/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Registro_lol/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"Registro_lol/registro.html" ,  {"form":form})
