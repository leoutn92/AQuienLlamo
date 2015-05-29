import datetime
class usuario:
	def __init__(self,NomUsuario=None,Contrasenia=None,Nombre=None,Apellido=None,Direccion=None,Telefono=None,Email=None,dic=None):
	 if dic==None:
	  self.NomUsuario=NomUsuario
	  self.Contrasenia=Contrasenia
	  self.Nombre=Nombre
	  self.Apellido=Apellido 
	  self.Direccion=Direccion
	  self.Telefono=Telefono
	  self.Email=Email
	 else:
	  self.NomUsuario=dic['NomUsuario']
	  self.Contrasenia=dic['Contrasenia']
	  self.Nombre=dic['Nombre']
	  self.Apellido=dic['Apellido'] 
	  self.Direccion=dic['Direccion']
	  self.Telefono=dic['Telefono']
	  self.Email=dic['Email']
	 self.FechaRegistro=datetime.datetime.now()
	 
	def login(self,NomUser,Contrasenia):
		if ((self.NomUsuario==NomUser) and (self.Contrasenia==Contrasenia)):
			return True
		return False		
	def sos(self,NomUser):
		if self.NomUsuario==NomUser:
			return True
		return False
	def isAdmin(self):
	 return False
	def isProveedor(self):
	 return False
	def isCliente(self):
	 return False
class Admin(usuario):
 def isAdmin(self):
  return True
class Cliente(usuario):
 def isCliente(self):
  return True

class Proveedor(usuario):
	def __init__(self,NomUsuario=None,Contrasenia=None,Nombre=None,Apellido=None,Direccion=None,Telefono=None,Email=None,NomEmpresa=None,CUIL=None,dic=None):
		usuario.__init__(self,NomUsuario,Contrasenia,Nombre,Apellido,Direccion,Telefono,Email,dic)
		if dic!=None:
		 self.NomEmpresa=dic['NomEmpresa']
		 self.CUIL=dic['CUIL']
		else:
		 self.NomEmpresa=NomEmpresa
		 self.CUIL=CUIL
	def isProveedor(self):
		return True
class Servicio:
 categorias=['pintores','plomeros','reparacion de aire acondicionado']
 estados=['disponible','no disponible']
 def __init__(self,categoria):
  if not (categoria in Servicio.categorias):
   raise MiError('no existe la categoria')
  else:
   self.categoria=categoria
   self.estado='disponible'
 def nuevaCat(self,cat):
   if not (categoria in categorias):
    self.categorias.append(cat)
   else:
    raise MiError('ya existe la categoria')