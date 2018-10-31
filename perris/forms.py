from django import forms
#Importamos el Modelo de Peros_Rescatados
from .models import Perros_Rescatados



#Crear el formulario de Perro Rescatado 

class Perro_RescatadoForm(forms.ModelForm):
	class Meta:
		model=Perros_Rescatados
		fields=('fotografia_perro','nombre_perro' , 'raza_predominante' , 'descripcion','estado', )	

