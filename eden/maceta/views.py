from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Maceta,Plantas,LogsTemperatura,LogsValvula,LogsLuminosidad,LogsHumedad
from .serializers import *
import coreapi

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class Macetizer():
	def get_variables(ipMaceta):
		"""
		Obtener las variables de temperatura, luminosidad, enviadas desde la maceta
		"""
		#response = client.get('http://bibliotecac.upbbga.edu.co/rest/info.php?uid=sombra')
		ip = ipMaceta
		client = coreapi.Client()
		response = self.client.get('http://'+ip+'/')
		print(response)

	def regar_macetica(ipMaceta):
		"""
		Hacer la peticion GET para regar la maceta
		"""
		ip = ipMaceta
		client = coreapi.Client()
		response = client.get('http://'+ip+'/digital/0/1')
		print(response)
		return response

@csrf_exempt
def variables_list(request,pkMaceta):

	#Enviar al usuario el ultimo registro de las variables

    try:
        temperatura = LogsTemperatura.objects.filter(maceta_id= pkMaceta).latest("id")
        humedad = LogsHumedad.objects.filter(maceta_id= pkMaceta).latest("id")
        luminosidad = LogsLuminosidad.objects.filter(maceta_id= pkMaceta).latest("id")
    except Maceta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = MacetaSerializer(variables)
        return JSONResponse(serializer.data)

@csrf_exempt
def registrar_maceta(request):
    #Registrar una nueva maceta
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            usuario = usuario.objects.get(id=data.idUsuario)
            serializer = MacetaSerializer(data=data)
            serializer.User = usuario
        except usuario.DoesNotExist:
            return HttpResponse(status=404)
        if serializer.is_valid():
			#guardar en la DB
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def registrar_usuario(request):
	"""
	Registrar un nuevo usuario
	"""
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			#guardar en la DB
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def regar_maceta(request,pkUser):
	"""
	El usuario presiono el boton de regar maceta
	"""
	try:
		usuario = usuario.User.objects.get(idUser = pkUser)
	except User.DoesNotExist:
		print("FUCKING HELL")
		return HttpResponse(status=404)


	if request.method == 'GET':
		return JSONResponse(Macetizer.regar_macetica('172.20.10.3'))
