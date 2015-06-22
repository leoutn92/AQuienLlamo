from django.shortcuts import render_to_response,render,HttpResponseRedirect
from django.template.context_processors import csrf
from register.models import Usuario,Cliente,Proveedor,Servicio
from django.views.generic import CreateView
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
			return render(request,'registro_p.html',{'errorUser0':'El usuario ya existe','errorEmpresa':''})
		usuario=Usuario(usuario=nomUsuario,contrasenia=contrasenia)
		usuario.save()
		cliente=Cliente(usuario=usuario,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono,email=email)
		cliente.save()
		prov=Proveedor(cliente=cliente,nomEmpresa=nomEmp,CUIL=cuil)
		query=Proveedor.objects.filter(nomEmpresa=nomEmp)
		if query:
			return render(request,'register_p.html',{'errorEmpresa':'la empresa ya existe','errorUser0':' '})
		prov.save()
		return HttpResponseRedirect('/AQuienLlamo/register/prov/regServicio')
	return render(request,'register_p.html')
	
class RegServicio(CreateView):
	template_name = 'regServicio.html'
	model = Servicio
	fields=['categoria','descripcion','precioBase']	
