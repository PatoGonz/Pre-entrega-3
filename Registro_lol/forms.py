from django import forms

class Crear_campeon_form(forms.Form):
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

    
                  