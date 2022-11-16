from django.urls import path
from MiApp.views import index, nuevo_deporte, nuevo_profesor, nuevo_alumno, buscar_CLUB, buscar_profesor 
from .forms import club_deportivoForm, profesorForm, alumnoForm


urlpatterns = [
    path('', index),
    path('nuevo_deporte/', nuevo_deporte, name='Nuevo Deporte'),
    path('nuevo_profesor/', nuevo_profesor, name='Nuevo Profesor'),
    path('nuevo_alumno/', nuevo_alumno, name='Nuevo Alumno'),
    path('buscar_CLUB/', buscar_CLUB, name='buscar CLUB'),
    path('buscar_profesor/', buscar_profesor, name='buscar PROFESOR'),
    path('club_deportivoForm/', club_deportivoForm),
    path('profesorForm/', profesorForm),
    path('alumnoForm/', alumnoForm),
]