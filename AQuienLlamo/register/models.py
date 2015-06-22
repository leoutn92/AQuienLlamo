from django.db import models
from django.contrib import admin
class Usuario(models.Model):
	usuario=models.CharField(max_length=30,unique=True)
	contrasenia=models.CharField(max_length=30)
	fechaRegistro=models.DateTimeField(auto_now_add=True)
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
class Categoria (models.Model):
	descripcion=models.CharField(max_length=50)
	def __str__(self):
		return self.descripcion
class Estado (models.Model):
	descripcion=models.CharField(max_length=50)
	def __str__(self):
		return self.descripcion
class Servicio (models.Model):
	proveedor=models.ForeignKey(Proveedor)
	descripcion=models.CharField(max_length=50)
	precioBase=models.IntegerField(null=False)
	categoria=models.ForeignKey(Categoria)
	estado=models.ForeignKey(Estado)
class Pedido(models.Model):
    descripcion=models.CharField(max_length=50)
    fechaPedido=models.DateTimeField(auto_now_add=True)
    Servicio=models.ForeignKey(Servicio)
    cliente=models.ForeignKey(Cliente)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Estado)
admin.site.register(Servicio)
admin.site.register(Pedido)
admin.site.register(Categoria)