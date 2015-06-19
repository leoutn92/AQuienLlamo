from django.shortcuts import render
from register.models import Usuario,Cliente,Proveedor
def welcome(request):
	return render(request,'auth.html')
