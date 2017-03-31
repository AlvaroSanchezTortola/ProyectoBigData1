from django.conf.urls import url


from colegiobd import views as colegiobd_views

urlpatterns = [
    url(r'^cursos', colegiobd_views.CursoLista, name='cursos'),
    url(r'^departamentos', colegiobd_views.DepartamentoLista, name='departamentos'),
    url(r'^profesores', colegiobd_views.ProfesoresLista, name='profesores'),
    url(r'^new/curso', colegiobd_views.CursoNuevo, name='nuevo_curso'),
    url(r'^new/profesor', colegiobd_views.ProfesorNuevo, name='nuevo_profesor'),
    url(r'^new/departamento', colegiobd_views.DepartamentoNuevo, name='nuevo_departamento'),
]