from __future__ import unicode_literals
from mongoengine import *
from django.db import models

# Create your models here.			

class Curso(EmbeddedDocument):
	"""docstring for Curso"""
	nombre = StringField(max_length = 100)
	nivel = StringField(max_length = 20)
	descripcion = StringField(max_length = 300)	

class Profesor(EmbeddedDocument):
	nombre = StringField(max_length = 50)
	direccion = StringField(max_length = 200)
	telefono = IntField()
	cursos = ListField(EmbeddedDocumentField(Curso))
	
class Departamento(Document):
	"""docstring for Departamento"""
	nombre = StringField(max_length = 100)
	director = StringField(max_length = 50)
	descripcion = StringField(max_length = 300)
	profesores = ListField(EmbeddedDocumentField(Profesor))
		
				

