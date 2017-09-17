# fuente: http://levipy.com/crear-api-rest-con-django-rest-framework/
from rest_framework import serializers
from .models import *
from usuario.models import *

class MacetaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Maceta
		fields = ("id",'tipoPlanta','fechaDePlantacion','primeraCosecha','User')

class PlantasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Plantas
		fields = ('id','nombre')

class LogsTemperaturaSerializer(serializers.ModelSerializer):
	class Meta:
		model = LogsTemperatura
		fields = ('id','id_maceta','fecha','valor')

class LogsValvulaSerializer(serializers.ModelSerializer):
	class Meta:
		model = LogsValvula
		fields = ('id','id_maceta','fecha','valor')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','contraseña','nombre','email','ciudad','fechaNacimiento')
