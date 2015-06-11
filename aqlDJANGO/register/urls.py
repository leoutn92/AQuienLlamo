from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','register.views.register'),
    url(r'/cli$','register.views.register_cli'),
    url(r'/prov$','register.views.register_prov')
]