from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from register.models import Usuario,Cliente
def register(request):
    return render_to_response('registro_c.html')
def register_cli(request):
	nomUsuario=request.GET['usuario']
	contrasenia=request.GET['contrasenia']
	nombre=request.GET['nombre']
	apellido=request.GET['apellido']
	direccion=request.GET['direccion']
	telefono=request.GET['telefono']
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
	cuil=request.GET["cuil"]
	nomEmp=request.GET["nomEmpresa"]
	usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
	usuario.save()
	cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
	cliente.save()
	prov=Proveedor()

    return render_to_response('registro_c.html')
