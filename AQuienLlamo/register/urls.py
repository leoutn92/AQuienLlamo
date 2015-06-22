from django.conf.urls import include, url
from django.contrib import admin
from .views import  RegServicio
urlpatterns = [
    url(r'^$','register.views.register'),
    url(r'/cli','register.views.register_cli'),
    url(r'/prov','register.views.register_prov'),
    url(r'^regservicio/$' , RegServicio.as_view()), 
]
