import re
from MainAQL import *
class Vista:
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
 def listar(self,tit,lista):
  print(tit)
  j=1
  for i in lista:
   print('%s-%s'%(j,i))
   j=j+1
  ops=int(input())
  while not (ops in range(1,j)):
   listar(ops)
  return lista[ops-1]
class VistaPrincipal(Vista):
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
  	print('Solo se permiten letras')
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
 def registrarCliente(self):
  print('Bienvenido al registro de clientes de A Quien Llamo')
  dic=self.cargarCliente()
  ops=self.ops('desea \n c-confirmar  de cliente? \n x-cancelar operacion? ','c','x')
  if (ops=='c'):
   try:
    self.main.agregarCliente(dic)
    print('cliente agregado exitosamente')
   except:
    print('ya existe este nombre de usuario')
 def registrarServicios(self,prov):
  print('al registrarte como proveedor necesitas agregar los servicios que brindas')
  categorias=self.main.verCateServ()
  lista=list()
  lista.extend(categorias)
  lista.append('mi servicio no entra en ninguna de esas categorias')
  ops=self.listar('estas son algunas de los servicios que brindan otros proveedores de AQL',lista)
  if (ops in categorias):
   try:
    self.main.agregarServicio(prov,categorias[ops-1])
    print('servicio agregado exitosamente')
    ops=self.ops('Desea agregar otro servicio?(si\no) ','si','no')
    if ops=='si':
     self.agregarServicios(prov)
   except MiError as e:
    print(e)
    self.agregarServicios(prov)
  else:
   cate=input('ingrese nueva categoria: ')
   try:
    self.main.agregarCategoria(cate)
    print('categoria agregada exitosamente')
   except MiError as e:
    print(e)
    self.agregarServicios(prov)       
 def registrarProv(self):
  print('Bienvenido al registro de proveedores de A Quien Llamo')
  dic=self.genDic('NomUsuario','Contrasenia','Nombre','Apellido','Direccion','Telefono','Email','NomEmpresa','CUIL')
  ops=self.ops('desea \n c-confirmar datos de Proveedor? \n x-cancelar operacion? \n','c','x')
  if (ops=='c'):
   try:
    self.main.agregarCliente(dic)
    print('proveedor registrado exitosamente')
    self.registrarServicios(dic['NomUsuario'])
   except MiError as e:
    print(e)
 def registrar(self):
  ops=self.ops('desea registrarse \n c-como cliente? \n p-como proveedor? \n v-volver al menu principal? \n','c','p','v')
  if (ops=='c'):
   self.registrarCliente()
  elif (ops=='p'):
   self.registrarProv()
 def login(self):
  NomUser=input('ingrese nombre de usuario: ')
  Contrasenia=input('ingrese contrasenia: ')
  user=self.main.login(NomUser,Contrasenia)
  if user==None:
   print('usuario o contrasenia no es valida')
   ops=self.ops('Desea: \n i-intentarlo nuevamente \n m-volver a menu principal\n','i','m')
   if ops=='i':
    self.login()
   else:
    self.regLogin()
  else:
   tuser=self.main.tipoUser(user)
   if tuser=='admin':
    pass
   elif tuser=='cliente':
    VistaCliente(self.main)
   elif tuser=='proveedor':
    pass
 def regLogin(self):
  ops=self.ops('desea \n r-registrarse? \n l-loguearse? \n x-salir? \n','r','l','x')
  while (ops!='x'):
   if (ops=='l'):
    self.login()
   elif (ops=='r'):
    self.registrar()
   ops=self.ops('desea \n r-registrarse? \n l-loguearse? \n x-salir? \n','r','l','x')
 def __init__(self):
  self.main=Main()
  self.regLogin()
class VistaCliente(Vista):
  def MenuServicios(self):
   ops=self.ops('desea \n c-buscar servicios por categoria \n n-buscar servicios por nombre \n r-ver servicios recientemente solicitados \n v-volver al menu principal \n','c','n','r')
   if ops=='c':
    categorias=self.main.verCateServ()
    opsiones=list()
    opsiones.extend(categorias)
    opsiones.append('agregar nueva categoria')
    ops=self.listar('seleccione una opsion',opsiones)
    if ops in categorias:
     opsiones=self.main.buscarServXCat(ops)
     if opsiones==None:
      print('No hay servicios disponibles')
     else:
      for i in opsiones:
       linea=''
       for x in i:
        linea=linea+x
        linea=linea+': '
        linea=linea+i[x]
        linea=linea+' '
       print(linea)
  def opsCliente(self):
   print('Bienvenido al menu de clientes de AQL')
   ops=self.ops('desea \n s-ver servicios \n p-ver pedidos \n y-lo quiero ya \n e-editar perfil \n x-salir \n','s','p','y','e','x')
   while ops!='x':
    if ops=='s':
     self.MenuServicios()
    ops=self.ops('desea \n s-ver servicios \n p-ver pedidos \n y-lo quiero ya \n e-editar perfil \n x-salir \n','s','p','y','e','x')
  def __init__(self,main):
   self.main=main
   self.opsCliente()
VistaPrincipal=VistaPrincipal()  