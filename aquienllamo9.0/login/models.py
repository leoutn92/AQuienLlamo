from django.db import models
from django.contrib.auth.models import User



class Usuario(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length= 50) 
	apellido = models.CharField(max_length= 50)
	dni=  models.IntegerField( null = False)
	email= models.EmailField (max_length= 300)
	telefono = models.IntegerField(max_length=10)
	def __unicode__(self):
		return self.usuario.username


