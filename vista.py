import re
import datetime
from MainAQL import *
class Vista:
 def isCUIL(self,a):
  return (a.isdigit() and (len(a)==11))
 def isTelephone(self,a):
  return (a.isdigit() & (len(a)==10))
 def isEmail(self,a):
    return re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',a.lower())     
 def genDic(self,*keys):
  ndic=dict()
  for i in keys:
   print('ingrese %s '%i)
   ndic[i]=input()
  return ndic   
 def ops(self,a,*args):
  ops=input(a)
  while not ( ops in args):
   ops=input(a)
  return ops
 def menu(self,tit,lista):
  print(tit)
  j=1
  for i in lista:
   print('%s-%s'%(j,i))
   j=j+1
  ops=int(input())
  while not (ops in range(1,j)):
   listar(ops)
  return lista[ops-1]
 def cargarUser(self):
  dic=dict()
  dic['NomUsuario']=input('Ingrese nombre usuario: ')
  dic['Contrasenia']=input('Ingrese contrasenia usuario: ')
  dic['Nombre']=input('Ingrese nombre: ')
  while not dic['Nombre'].isalpha():
  	print('Solo se permiten letras')
  	dic['Nombre']=input('Ingrese nombre: ')
  dic['Apellido']=input('Ingrese Apellido: ')
  while not dic['Apellido'] .isalpha ():
  	print('Solo se permiten ')
  	dic['Apellido'] =input('Ingrese Apellido: ')
  dic['Pais']=input('Ingrese pais: ')
  while not dic['Pais'].isalpha():
  	print('Solo se permiten letras')
  	dic['Pais'] =input('Ingrese pais: ')
  dic['Provincia']=input('Ingrese provincia: ')
  while not dic['Provincia'].isalpha():
  	print('Solo se permiten letras')
  	dic['Provincia'] =input('Ingrese provincia: ')
  dic['Localidad']=input('Ingrese localidad: ')
  while not dic['Localidad'] .isalpha():
  	print('Solo se permiten localidad')
  	dic['Localidad'] =input('Ingrese localidad: ')
  Calle=input('Ingrese direccion: ')
  while not Calle.isalpha():
  	print('Solo se permiten letras')
  	Calle=input('Ingrese calle: ')
  Direccion=Calle
  Numero=input('Ingrese numero: ')
  while not Numero.isdigit():
  	print('Solo se permiten nomeros')
  	Numero=input('Ingrese numero: ')
  dic['Direccion']=Direccion+' '+Numero
  ops=self.ops('Desea ingrezar piso? (si/no)','si','no')
  if ops=='si':
  	piso=input('Ingrese piso: ')
  	dic['Direccion'] = dic['Direccion'] +' '+piso
  dic['Telefono']=input('Ingrese numero de telefono: ')
  while not (self.isTelephone(dic['Telefono'])):
  	print('Solo se permiten hasta 10 numeros')
  	dic['Telefono']=input('Ingrese numero de telefono: ')
  dic['Email']=input('Ingrese email: ')
  while not self.isEmail(dic['Email']):
  	print('Direccion de mail no valida')
  	dic['Email']=input('Ingrese email: ')
  return dic
 def cargarCliente(self):
  dic=self.cargarUser()
  return dic
 def cargarProveedor(self):
  dic=self.cargarUser()
  dic['NomEmpresa']=input('ingrese nombre de empresa')
  dic['CUIL']=input('ingrese CUIL')
  while not self.isCUIL(dic['CUIL']):
   print('el cuil es un campo numerico de 11 digitos')
   dic['CUIL']=input('ingrese CUIL')
  return dic
 def cargardigitos(self,mensaje):
  dig=input(mensaje)
  while not (dig.isdigit()):
   dig=input(mensaje)
  dig=int(dig)
  return dig
 def cargarFecha(self):
  dia=self.cargardigitos('ingrese dia: ')
  mes=self.cargardigitos('ingrese mes: ')
  anio=self.cargardigitos('ingrese anio: ')
  fecha=datetime.datetime(anio,mes,dia)
  ops=self.ops('desea añadir hora? ','si','no')
  if (ops=='si'):
   hora=self.cargardigitos('ingrese hora: ')
   fecha=datetime.datetime(anio,mes,dia,hora)
  return fecha
 
   