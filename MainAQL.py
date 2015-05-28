import datetime
from usuario import *
from pedidos import *
from Excepsiones import*
class Main:
	def __init__(self):
		self.usuarios=[]
		self.servXprov=[]
		self.pedidos=[]
		self.cargarUsuarios()
	def cargarUsuarios(self):
	 dic=dict()
	 dic['NomUsuario']='juan'
	 dic['Contrasenia']='contrasenia'
	 dic['Nombre']='juan'
	 dic['Apellido']='fernandez' 
	 dic['Direccion']='cordoba 400'
	 dic['Telefono']='3644657666'
	 dic['Email']='juanfer@gmail.com'
	 cliente=Cliente(dic=dic)
	 self.agregarUsuario(cliente)
	 proveedor=Proveedor('colores','Contrasenia','Pedro','Fernandez','calle falsa 123','3624343537','pedrofer@gmail.com','colores','34569871234')
	 self.agregarUsuario(proveedor)
	 self.agregarServicio(proveedor.NomUsuario,'pintores')
	 proveedor1=Proveedor('colorH','Contrasenia','jose','Fernandez','calle falsa 133','3624444537','josefer@gmail.com','color humano','34599871234')
	 self.agregarUsuario(proveedor1)
	 self.agregarServicio(proveedor1.NomUsuario,'pintores')
	 admin=Admin('Admin','Contrasenia','Nombre','Apellido','Direccion','Telefono','Email')
	 self.agregarUsuario(admin)
	def existeUsuario(self,NomUser):
		for i in self.usuarios:
			if i.sos(NomUser):
				return True
		return False
	def login(self,NomUser,Contrasenia):
	 for i in self.usuarios:
	  if i.login(NomUser,Contrasenia):
	   return i
	 return None
	def agregarUsuario(self,usuario):
	 if self.existeUsuario(usuario.NomUsuario):
	  raise MiError('El usuario ya existe') 
	 self.usuarios.append(usuario)
	def agregarCliente(self,dic):
	  cliente=Cliente(dic=dic)
	  self.agregarUsuario(cliente)
	def agregarProv(self,dic):
	  prov=Prov(dic=dic)
	  self.agregarUsuario(Prov)
	def buscarUser(self,user):
	 for i in self.usuarios:
	  if (i.NomUsuario==user):
	   return i
	 return None
	def buscarCliente(self,cliente):
	 cliente=self.buscarUser(cliente)
	 if cliente!=None:
	  if cliente.isCliente():
	   return cliente
	 return None
	def buscarProv(self,prov):
	 prove=self.buscarUser(prov)
	 if prove!=None:
	  if prove.isProveedor():
	   return prove
	 return None
	def tipoUser(self,user):
	 if user.isAdmin():
	  return 'admin'
	 elif user.isCliente():
	  return 'cliente'
	 elif user.isProveedor():
	  return 'proveedor'
	def verServProv(self,prov,cat=None):
	 if cat==None:
	  for i in self.servXprov:
	   if i['proveedor']==prov:
	    servicios=i['servicios']
	    return servicios
	  return None
	 else:
	  for i in self.servXprov:
	   if i['proveedor']==prov:
	    servicios=i['servicios']
	    for j in servicios:
	     if (j.categoria==cat):
	      return j
	    return None
	def buscarServXCat(self,cat):
	 busqueda=[]
	 servicios=self.servXprov
	 for i in servicios:
	  for j in i['servicios']:
	   if j.categoria==cat:
	    if j.estado=='disponible':
	     dic=dict()
	     dic['Proveedor']=i['proveedor'].NomEmpresa
	     dic['Telefono']= i['proveedor'].Telefono
	     dic['Email']= i['proveedor'].Email
	     dic['Direccion']=i['proveedor'].Direccion
	     busqueda.append(dic)
	 return busqueda  
	def verCateServ(self):
	 return sorted(Servicio.categorias)
	def agregarCategoria(self,cat):
	 if (cat in Servicio.categorias):
	  raise MiError('Esta categoria ya existe')
	 Servicio.categorias.append(cat)
	def agregarServicio(self,prov,cat):
	 objProv=self.buscarProv(prov)
<<<<<<< HEAD
	 servicios=self.
=======
	 servicios=self.verServProv(objProv)
	 if servicios==None:
	  dicServ=dict()
	  dicServ['proveedor']=objProv
	  servicio=Servicio(cat)
	  dicServ['servicios']=[servicio]
	  self.servXprov.append(dicServ)
	 else:
	  for i in servicios:
	   if(i.categoria==cat):
	    raise MiError('servicio ya cargado')
	   servicio=Servicio(cat)
	   self.servicios.append(servicio)
	def mostrarUsuarios(self):
	 print (self.usuarios)
	def agregarPedido(self,dic,cliente,proveedor,categoria):
	 pedido=Pedido(dic)
	 cliente=self.buscarCliente(cliente)
	 proveedor=self.buscarProv(proveedor)
	 servicio=self.verServProv(proveedor,categoria)
	 if ((servicio!=None)and(cliente!=None)):
	  dic=dict()
	  dic['servicio']=servicio
	  dic['cliente']=cliente
	  dic['pedido']=pedido
	  self.pedidos.append(dic)
	 
	 
   
>>>>>>> 80a147fa562aaa0581335212716e1a81a0efe2fc
