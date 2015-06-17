from django.shortcuts import render
from register.models import Usuario,Cliente,Proveedor
def validar(request):
	if request.method=="POST":
		nomUsuario=request.POST["username"]
		contrasenia=request.POST["password"]
		usuario=Usuario.objects.get(usuario=nomUsuario)
		if (usuario.contrasenia==contrasenia):
			cliente=Cliente.objects.get(usuario=usuario)
			return render(request,'registroExitoso.html',{'nombre':cliente.nombre})