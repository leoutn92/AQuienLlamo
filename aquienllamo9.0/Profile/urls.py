from . import views
from django.conf.urls import include, url 
urlpatterns = [
	url(r'^$' , views.Profile ,name='profile'),
	url(r'^registro_proveedor/$' , views.Registrarse.as_view() ,name='registerProveedor'),
	url(r'^registro_proveedor/OK$' , views.register ,name='registerProveedor'),
]