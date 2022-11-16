from django.shortcuts import render
from django.http import HttpResponse
from .models import profesor, club_deportivo, alumno
from .forms import club_deportivoForm, profesorForm, alumnoForm


def index(request):
   return render(request, 'index.html')

######### BUSQUEDAS ##########


def buscar_profesor(request):

   consulta_profesor = profesor(deporte=['deporte'], nombre=['nombre'], DNI=['DNI'])
   
   return render(request, 'consulta_profesor.html' ,{'profesor':[consulta_profesor]})

def buscar_CLUB(request):

   if request.GET.get('deporte', False):
      deporte = request.GET['deporte']
      CLUB = club_deportivo.objects.filter(club_deportivo__icontains=club_deportivo)
      return render(request, 'consulta_deporte.html', {'CLUB': CLUB})

   else:
      respuesta = 'no hay datos ingresados...'
      return render(request, 'consulta_deporte.html', {'respuesta': respuesta})



######### INGRESOS DE DEPORTE ##########
def nuevo_deporte(request):
   if request.method == 'POST':
      
      formulario_ND = club_deportivoForm(request.POST)
   
      if formulario_ND.is_valid():
         
         formulario_ND_limpio = formulario_ND.cleaned_data
         
         nuevo_profesor = club_deportivo(deporte=formulario_ND_limpio['deporte'], nombre=formulario_ND_limpio['nombre'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_ND = club_deportivoForm()
      
   return render(request, 'nuevo_deporte.html', {'formulario_ND': formulario_ND})

######### INGRESOS DE PROFESORES ##########
def nuevo_profesor(request):
   if request.method == 'POST':
      
      formulario_NP = profesorForm(request.POST)
      
      if formulario_NP.is_valid():
         
         formulario_NP_limpio = formulario_NP.cleaned_data
         
         nuevo_profesor = profesor(deporte=formulario_NP_limpio['deporte'], nombre=formulario_NP_limpio['nombre'], DNI=formulario_NP_limpio['DNI'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_NP = profesorForm()
      
   return render(request, 'nuevo_profesor.html', {'formulario_NP': formulario_NP})

######### INGRESOS DE ALUMNOSS ##########
def nuevo_alumno(request):
   if request.method == 'POST':
      
      formulario_NA = alumnoForm(request.POST)
      
      if formulario_NA.is_valid():
         
         formulario_NA_limpio = formulario_NA.cleaned_data
         
         nuevo_alumno = alumno(deporte=formulario_NA_limpio['deporte'], nombre=formulario_NA_limpio['nombre'], DNI=formulario_NA_limpio['DNI'])
         
         nuevo_alumno.save()
         
         return render(request, 'index.html')

   else:
      formulario_NA = alumnoForm()
      
   return render(request, 'nuevo_alumno.html', {'formulario_NA': formulario_NA})



#consulta_profesor = profesor(deporte=['deporte'], nombre=['nombre'], DNI=['DNI'])
   
#  return render(request, 'consulta_profesor.html' ,{'profesor':[consulta_profesor]})
