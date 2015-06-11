from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from register.models import Usuario,Cliente,Proveedor
def register(request):
    return render_to_response('registro_c.html')
def validCli(request,nomUsuario):
	query=Usuario.objects.filter(usuario=nomUsuario)
	if query:
		return render_to_response('registro_c.html',{'errorUser':'El usuario ya existe'})
def register_cli(request):
	nomUsuario=request.GET['usuario']
	contrasenia=request.GET['contrasenia']
	nombre=request.GET['nombre']
	apellido=request.GET['apellido']
	direccion=request.GET['direccion']
	telefono=request.GET['telefono']
	validCli(request,nomUsuario)
	usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
	usuario.save()
	cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
	cliente.save()
	return render_to_response('registroExitoso.html')
def register_prov(request):
	nomUsuario=request.GET['usuario']
	contrasenia=request.GET['contrasenia']
	nombre=request.GET['nombre']
	apellido=request.GET['apellido']
	direccion=request.GET['direccion']
	telefono=request.GET['telefono']
	cuil=request.GET['cuil']
	nomEmp=request.GET['nomEmpresa']
	validCli(request,nomUsuario)
	query=Usuario.objects.filter(usuario=nomUsuario)
	if query:
		return render_to_response('registro_c.html',{'errorUser0':'El usuario ya existe','errorEmpresa':'la empresa ya existe'})
	usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
	usuario.save()
	cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
	cliente.save()
	prov=Proveedor(cliente=cliente,nomEmpresa=nomEmp,CUIL=cuil)
	query=Proveedor.objects.filter(nomEmpresa=nomEmp)
	if query:
		return render_to_response('registro_c.html',{'errorEmpresa':'la empresa ya existe','errorUser0':' '})
	prov.save()
	return render_to_response('registroExitoso.html')
