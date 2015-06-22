from django.conf.urls import include, url
from django.contrib import admin
from register.views import RegServicio
urlpatterns = [
    url(r'^$','register.views.register'),
    url(r'/cli','register.views.register_cli'),
    url(r'/prov$','register.views.register_prov'),
    url(r'/prov/regServicio$' , RegServicio.as_view()), 
]