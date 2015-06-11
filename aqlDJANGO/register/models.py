from django.db import models
class Usuario(models.Model):
	usuario=models.CharField(max_length=30,unique=True)
	contrasenia=models.CharField(max_length=30)
class Cliente(models.Model):
	usuario=models.ForeignKey(Usuario)	
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	direccion=models.CharField(max_length=30)
	telefono=models.IntegerField()
class Proveedor(models.Model):
	cliente=models.ForeignKey(Cliente)
	nomEmpresa=models.CharField(max_length=30,unique=True)
	CUIL=models.IntegerField()
