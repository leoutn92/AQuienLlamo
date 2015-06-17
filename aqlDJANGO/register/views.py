from django.shortcuts import render_to_response,render
from django.template.context_processors import csrf
from register.models import Usuario,Cliente,Proveedor
def register(request):
    return render(request,'registro_r.html')
def register_cli(request):
	nomUsuario=request.POST['usuario']
	contrasenia=request.POST['contrasenia']
	nombre=request.POST['nombre']
	apellido=request.POST['apellido']
	direccion=request.POST['direccion']
	telefono=request.POST['telefono']
	query=Usuario.objects.filter(usuario=nomUsuario)
	if query:
		return render(request,'registro_r.html')
	usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
	usuario.save()
	cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
	cliente.save()
	return render(request,'registroExitoso.html')
def register_prov(request):
	nomUsuario=request.GET['usuarioP']
	contrasenia=request.GET['contraseniaP']
	nombre=request.GET['nombreP']
	apellido=request.GET['apellidoP']
	direccion=request.GET['direccionP']
	telefono=request.GET['telefonoP']
	cuil=request.GET['cuilP']
	nomEmp=request.GET['nomEmpresaP']
	query=Usuario.objects.filter(usuario=nomUsuario)
	if query:
		return render(request,'registro_r.html',{'errorUser0':'El usuario ya existe','errorEmpresa':''})
	usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
	usuario.save()
	cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono)
	cliente.save()
	prov=Proveedor(cliente=cliente,nomEmpresa=nomEmp,CUIL=cuil)
	query=Proveedor.objects.filter(nomEmpresa=nomEmp)
	if query:
		return render(request,'registro_r.html',{'errorEmpresa':'la empresa ya existe','errorUser0':' '})
	prov.save()
	return render(request,'registroExitoso.html')
