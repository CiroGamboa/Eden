from django.conf.urls import url
from maceta import views


urlpatterns = [
	url(r'^getVariables/(?P<pkMaceta>[0-9]+)/$',views.variables_list),
	url(r'^regUser/$',views.registrar_usuario),
	url(r'^regMaceta/$',views.registrar_maceta),
	url(r'^regarMaceta/(?P<pkUser>[0-9]+)/$',views.regar_maceta),
]
