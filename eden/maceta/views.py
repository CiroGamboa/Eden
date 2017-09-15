from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Maceta,Plantas
from genEden.serializers import MacetaSerializer,UserSerializer
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
	"""
	Enviar al usuario el ultimo registro de las variables
	"""
	try:
		variables = Maceta.objects.filter(LogsTemperatura__LogsLuminosidad__LogsHumedad__maceta = pkMaceta)
	except Maceta.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = MacetaSerializer(variables)
		return JSONResponse(serializer.data)
