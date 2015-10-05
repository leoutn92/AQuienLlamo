from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
class Category(models.Model):
    Name = models.CharField(max_length=30,unique=True,primary_key=True)
    def __unicode__(self):
            return self.Name
class UserAQL(models.Model):
    User = models.OneToOneField(User)
    FirstName = models.CharField(max_length= 50) 
    LastName = models.CharField(max_length= 50)
    DNI=  models.IntegerField( null = False)
    Phone = models.IntegerField(max_length=10,default=0)
    Adress = models.CharField(max_length= 50,default='no tiene')
    Image = models.ImageField(upload_to= 'static/ImageUserAQL')
    def __unicode__(self):
        return self.FirstName+' '+self.LastName
class Service(models.Model):
    NameService= models.CharField(max_length=50,unique=True)
    User = models.ForeignKey(UserAQL)
    Category = models.ForeignKey(Category)
    DescriptionService = models.TextField(max_length= 500)
    Calification = models.PositiveIntegerField(validators=[MaxValueValidator(10)],default=0) 
    Phone = models.IntegerField()
    Email= models.EmailField (max_length= 300)
    Adress = models.CharField(max_length= 50)
    Image = models.ImageField(upload_to= 'static/ImageService')
    CreationDate = models.DateField(default=timezone.now())
    def __unicode__(self):
        return self.NameService
class Calification(models.Model):
    Service = models.ForeignKey(Service)
    User = models.ForeignKey(UserAQL)
    Value = models.PositiveIntegerField(validators=[MaxValueValidator(10)],default=0)
class Comment(models.Model):
    Service = models.ForeignKey(Service)
    User = models.ForeignKey(UserAQL)
    Opinion = models.TextField(max_length= 500)
    CreationDate = models.DateField(default=timezone.now())
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(UserAQL)
admin.site.register(Calification)
admin.site.register(Comment)