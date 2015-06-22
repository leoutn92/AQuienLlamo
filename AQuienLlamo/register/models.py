from django.db import models
from django.contrib import admin
class Usuario(models.Model):
	usuario=models.CharField(max_length=30,unique=True)
	contrasenia=models.CharField(max_length=30)
class Cliente(models.Model):
	usuario=models.ForeignKey(Usuario)	
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	direccion=models.CharField(max_length=30)
	telefono=models.IntegerField()
	email=models.EmailField()
class Proveedor(models.Model):
	cliente=models.OneToOneField(Cliente)
	nomEmpresa=models.CharField(max_length=30,unique=True)
	CUIL=models.IntegerField()
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Proveedor)