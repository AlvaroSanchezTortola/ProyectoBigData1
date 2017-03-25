#from django.contrib import admin
from mongoengine.django.auth import User

# Register your models here.
from django.contrib import admin
from .models import Curso, Profesor, Departamento

User.site.register(Curso)
User.site.register(Profesor)
User.site.register(Departamento)