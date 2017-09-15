from django.db import models

class User(models.Model):
    contraseña = models.CharField(max_length=32)
    nombre = models.CharField(max_length=32)
    email =  models.CharField(max_length=32)
    pais =  models.CharField(max_length=32)
    ciudad = models.CharField(max_length=32)
    fechaNacimiento = models.DateTimeField()

class fotos(models.Model):
    fotoUrl = models.CharField(max_length=32)
    usuario = models.ForeignKey('User',on_delete=models.CASCADE)

class libroUser(models.Model):
    usuario = models.ForeignKey('user',on_delete=models.CASCADE)
    libro = models.ForeignKey('Libros',on_delete=models.CASCADE)

class Libros(models.Model):
    titulo = models.CharField(max_length=32)
    cuerpo = models.CharField(max_length=300)
    autor = models.CharField(max_length=32)
    precio =  models.FloatField()
    editorial = models.CharField(max_length=32)
    fechaPublicacion = models.DateTimeField()
