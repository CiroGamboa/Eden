from django.db import models
from usuario.models import User

# Create your models here.

class Maceta(models.Model):

    tipoPlanta = models.ForeignKey('Plantas', on_delete= models.CASCADE)
    fechaDePlantacion= models.DateTimeField()
    primeraCosecha = models.DateTimeField()
    User = models.ForeignKey('usuario.User', on_delete=models.CASCADE)

class Plantas(models.Model):
    nombre = models.CharField(max_length=32)

class LogsTemperatura(models.Model):
    maceta =  models.ForeignKey('maceta',on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    valor = models.FloatField()

class LogsValvula(models.Model):
    maceta =  models.ForeignKey('maceta',on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    valor = models.FloatField()

class LogsLuminosidad(models.Model):
    maceta =  models.ForeignKey('maceta',on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    valor = models.FloatField()

class LogsHumedad(models.Model):
    maceta =  models.ForeignKey('maceta',on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    valor = models.FloatField()
