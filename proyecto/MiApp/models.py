from django.db import models

class club_deportivo(models.Model):
    deporte = models.CharField(max_length = 40)
    nombre = models.CharField(max_length = 40)
    
class profesor(models.Model):
    nombre = models.CharField(max_length = 40)
    deporte = models.CharField(max_length = 40)
    DNI = models.IntegerField()


class alumno(models.Model):
    deporte = models.CharField(max_length = 40)
    nombre = models.CharField(max_length = 40)
    DNI = models.IntegerField()
    
    
    