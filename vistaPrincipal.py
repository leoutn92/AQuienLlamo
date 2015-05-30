from vista import *
from vistaCliente import *
class VistaPrincipal(Vista):
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
  opsiones=list()
  opsiones.extend(categorias)
  opsiones.append('mi servicio no entra en ninguna de esas categorias')
  titulo='estas son algunas de los servicios que brindan otros proveedores de AQL'
  ops=self.menu(titulo,opsiones)
  if (ops in categorias):
   try:
    self.main.agregarServicio(prov,ops)
    print('servicio agregado exitosamente')
    ops=self.ops('Desea agregar otro servicio?(si\no) \n','si','no')
    if ops=='si':
     self.registrarServicios(prov)
   except MiError as e:
    print(e)
    self.registrarServicios(prov)
  else:
   cate=input('ingrese nueva categoria: ')
   try:
    self.main.agregarCategoria(cate)
    print('categoria agregada exitosamente')
    self.registrarServicios(prov)
   except MiError as e:
    print(e)
    self.registrarServicios(prov)       
 def registrarProv(self):
  print('Bienvenido al registro de proveedores de A Quien Llamo')
  dic=self.cargarProveedor()  
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
    VistaCliente(self.main,user)
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
VistaPrincipal=VistaPrincipal()