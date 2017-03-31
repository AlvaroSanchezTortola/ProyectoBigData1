from __future__ import unicode_literals
from mongoengine import *
from django.db import models

from djangotoolbox.fields import EmbeddedModelField
from djangotoolbox.fields import ListField
from .formField import ObjectListField

# Create your models here.			

class Curso(models.Model):
	nombre = StringField(max_length = 100)
	nivel = StringField(max_length = 20)
	descripcion = StringField(max_length = 300)
	def __unicode__(self):
		return '%s %s %s %s' % (self.nombre, self.nivel, self.descripcion, self.codigo)	

class EmbedOverrideField(EmbeddedModelField):
    def formfield(self, **kwargs):
		return models.Field.formfield(self, ObjectListField, **kwargs)

class Profesor(models.Model):
	nombre = StringField(max_length = 50)
	direccion = StringField(max_length = 200)
	telefono = IntField(255)
	codigo = models.CharField(max_length=255, unique=True)
	cursos = ListField(EmbeddedModelField('Curso'))
	def __unicode__(self):
		return '%s %s %s %s' % (self.nombre, self.direccion, self.telefono, self.codigo)	
	
class Departamento(models.Model):
	"""docstring for Departamento"""
	nombre = StringField(max_length = 100)
	director = StringField(max_length = 50)
	descripcion = StringField(max_length = 300)
	codigo = models.CharField(max_length=255, unique=True)
	profesores = ListField(EmbeddedModelField('Profesor'))
	def __unicode__(self):
	 	return '%s %s %s %s' % (self.nombre, self.director, self.descripcion,self.codigo)	
		
				

