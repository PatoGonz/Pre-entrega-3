from django.shortcuts import render
from django.http import HttpResponse
from Registro_lol.models import Crear_campeones, Crear_ward, Crear_mapa
from django.urls import reverse_lazy

# Create your views here.

def index(request):
	return render(request, "Registro_lol/index.html")

def Crear_campeones(request):
	return render(request, "Registro_lol/index.html")