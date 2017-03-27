from __future__ import unicode_literals
from mongoengine import *
from django.db import models

from djangotoolbox.fields import EmbeddedModelField
from djangotoolbox.fields import ListField

# Create your models here.			

class Curso(models.Model):
	"""docstring for Curso"""
	nombre = StringField(max_length = 100)
	nivel = StringField(max_length = 20)
	descripcion = StringField(max_length = 300)
	def __unicode__(self):
		return '%s %s %s' % (self.nombre, self.nivel, self.descripcion)	

class Profesor(models.Model):
	nombre = StringField(max_length = 50)
	direccion = StringField(max_length = 200)
	telefono = IntField()
	cursos = EmbeddedModelField('Curso')
	def __unicode__(self):
		return '%s %s %s %s' % (self.nombre, self.nivel, self.descripcion, self.cursos.nombre)	
	
class Departamento(models.Model):
	"""docstring for Departamento"""
	nombre = StringField(max_length = 100)
	director = StringField(max_length = 50)
	descripcion = StringField(max_length = 300)
	profesores = EmbeddedModelField('Profesor')
	def __unicode__(self):
		return '%s %s %s %s' % (self.nombre, self.director, self.descripcion, self.profesores.nombre)	
		
				

