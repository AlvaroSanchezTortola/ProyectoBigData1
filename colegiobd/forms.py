from django import forms
from colegiobd.models import  Curso

class CursoForm(forms.ModelForm):
  class Meta:
		model = Curso
		fields = ('nombre','nivel','descripcion')
class DepartamentoForm(forms.Form):
	nombre = forms.CharField()
	director = forms.CharField()
	descripcion = forms.CharField()
	profesor = forms.CharField()
        
class ProfesorForm(forms.Form):
	nombre = forms.CharField()
	direccion = forms.CharField()
	telefono = forms.CharField()
	cursos = forms.CharField()
