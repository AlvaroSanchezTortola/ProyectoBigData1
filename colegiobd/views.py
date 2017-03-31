from django.shortcuts import render
import mongoengine
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from colegiobd.models import Curso, Profesor, Departamento
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from colegiobd.forms import CursoForm, ProfesorForm, DepartamentoForm

# Create your views here.


#Curso--------------------------------------------------
def CursoLista(request):
    cursos = Curso.objects.all()
    return render(
        request,
        'cursos.html',
        {
            'cursos': cursos
        }
    )
def CursoNuevo(request):
	curso_form = CursoForm()
	if request.method == 'GET':
	    curso_form = CursoForm()
	elif request.method == 'POST':
	    curso_form = CursoForm(data=request.POST)
	    if curso_form.is_valid():
	        curso_form.save()
	        curso_form = CursoForm()


	return render(
	    request,
	    'form_curso.html',
	    {
	        'curso_form': curso_form
	    }
	)
def CursoEdit(request, pk1):
	curso = Curso.objects.get(pk=pk1)
	if request.method == 'GET':
	    curso_form = CursoForm(instance=curso)
	elif request.method == 'POST':
	    curso_form = CursoForm(request.POST)
	    Curso.objects.get(pk=pk1).delete()
	    if curso_form.is_valid():
	        curso.nombre = curso_form.instance.nombre
	        curso.nivel = curso_form.instance.nivel
	        curso.descripcion = curso_form.instance.descripcion
	        curso.save()
	        print curso
	else:
	    pass
	return render(
	    request,
	    'form_curso.html',
	    {
	        'curso_form': curso_form,
	    }
	)
def CursoDelete(request, pk1):
	curso = Curso.objects.get(pk=pk1)
	if(curso != None ):
		Curso.objects.get(pk=pk1).delete()
	cursos = Curso.objects.all()

	return render(
        request,
        'cursos.html',
        {
            'cursos': cursos
        }
    )
#----------------------------------------------------------------------------------------
#Profesor---------------------------------------------------------------------------------
def ProfesoresLista(request):
    profesores = Profesor.objects.all()
    return render(
        request,
        'profesores.html',
        {
            'profesores': profesores
        }
    )

def ProfesorNuevo(request):
	profesor_form = ProfesorForm()
	if request.method == 'GET':
	    profesor_form = ProfesorForm()
	elif request.method == 'POST':
	    profesor_form = ProfesorForm(data=request.POST)
	    if profesor_form.is_valid():
	    	nombre1 = profesor_form.cleaned_data['nombre']
	    	direccion = profesor_form.cleaned_data['direccion']
	    	telefono = profesor_form.cleaned_data['telefono']
	    	cursos=profesor_form.cleaned_data['cursos']
	    	cursos = cursos.split(',')
	    	listCursos = []
	    	for i in cursos:
	    		curso = Curso.objects.get(nombre=i.strip())
	    		listCursos.append(curso)
	    	profesor = Profesor(nombre=nombre1, direccion=direccion, telefono=telefono, curso=listCursos)
	        profesor.save()
	        profesor_form = ProfesorForm()


	return render(
	    request,
	    'form_profesor.html',
	    {
	        'profesor_form': profesor_form
	    }
	)

def ProfesorDelete(request, nombre):
	profesor = Profesor.objects.get(nombre=nombre)
	if(profesor != None ):
		Curso.objects.get(pk=pk1).delete()
	profesores = Profesor.objects.all()
	return render(
        request,
        'profesores.html',
        {
            'profesores': profesores
        }
    )

#------------------------------------------------------------------------------------------------------
def DepartamentoLista(request):
    departamentos = Departamento.objects.all()
    return render(
        request,
        'departamentos.html',
        {
            'departamentos': departamentos
        }
    )


def DepartamentoNuevo(request):
	departamento_form = DepartamentoForm()
	if request.method == 'GET':
	    departamento_form = DepartamentoForm()
	elif request.method == 'POST':
	    departamento_form = DepartamentoForm(data=request.POST)
	    if departamento_form.is_valid():
	       	nombre = departamento_form.cleaned_data['nombre']
	    	director = departamento_form.cleaned_data['director']
	    	descripcion = departamento_form.cleaned_data['descripcion']
	    	profesores=departamento_form.cleaned_data['profesores']
	    	profesores = profesores.split(',')
	    	listProfesores = []
	    	for i in profesores:
	    		profesor = Profesor.objects.get(nombre=i.strip())
	    		listCursos.append(profesor)
	    	profesor = Clase(nombre=nombre, director=director, descripcion=descripcion, profesores=listProfesores)
	        profesor.save()
	        profesor_form = ProfesorForm()
	return render(
	    request,
	    'form_departamento.html',
	    {
	        'departamento_form': departamento_form
	    }
	)