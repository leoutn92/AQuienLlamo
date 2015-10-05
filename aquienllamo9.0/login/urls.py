from django.conf.urls import patterns, include, url
from .views import Registrarse 
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import login
urlpatterns = [
	url(r'^$' , views.enter , name='login'),
	url(r'^salir/$' ,views.salir, name='logout'),
	url(r'^registro/$', Registrarse.as_view() , name = 'registro'),
	url(r'^registro/OK$', views.register , name = 'registro'),
]
  