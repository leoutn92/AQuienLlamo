from django.shortcuts import render_to_response,render
from django.template.context_processors import csrf
from register.models import Usuario,Cliente,Proveedor
def register(request):
    return render(request,'selRegistro.html')
def register_cli(request):
	if request.method=="POST":
		nomUsuario=request.POST['usuario']
		contrasenia=request.POST['contrasenia']
		nombre=request.POST['nombre']
		apellido=request.POST['apellido']
		direccion=request.POST['direccion']
		telefono=request.POST['telefono']
		email=request.POST['email']
		query=Usuario.objects.filter(usuario=nomUsuario)
		if query:
			return render(request,'registro_r.html')
		usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
		usuario.save()
		cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono,email=email)
		cliente.save()
		return render(request,'registroExitoso.html')
	return render(request,'registro_r.html')
def register_prov(request):
	if request.method=="POST":
		nomUsuario=request.POST['usuario']
		contrasenia=request.POST['contrasenia']
		nombre=request.POST['nombre']
		apellido=request.POST['apellido']
		direccion=request.POST['direccion']
		telefono=request.POST['telefono']
		cuil=request.POST['cuil']
		nomEmp=request.POST['nomEmpresa']
		email=request.POST['email']
		query=Usuario.objects.filter(usuario=nomUsuario)
		if query:
			return render(request,'registro_r.html',{'errorUser0':'El usuario ya existe','errorEmpresa':''})
		usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
		usuario.save()
		cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono,email=email)
		cliente.save()
		prov=Proveedor(cliente=cliente,nomEmpresa=nomEmp,CUIL=cuil)
		query=Proveedor.objects.filter(nomEmpresa=nomEmp)
		if query:
			return render(request,'registro_r.html',{'errorEmpresa':'la empresa ya existe','errorUser0':' '})
		prov.save()
		return render(request,'registroExitoso.html')
	return render(request,'register_p.html')