from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class Crear_campeon_form(LoginRequiredMixin, forms.Form):
    nombre_campeon = forms.CharField()
    dificultad_campeon = forms.IntegerField()
    descripcion_campeon = forms.CharField()

class Crear_ward_form(forms.Form):
    nombre_ward = forms.CharField()
    rango_vision = forms.IntegerField()
    descripcion_ward = forms.CharField()

class Crear_mapa_form(forms.Form):
    nombre_mapa = forms.CharField()
    cantidad_jugadores = forms.IntegerField()
    descripcion_mapa = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
    
                  