# Register your models here.
from django.contrib import admin
from .models import Curso, Profesor, Departamento

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Departamento)