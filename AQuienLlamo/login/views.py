from django.shortcuts import render
from register.models import Usuario,Cliente,Proveedor
def validar(request):
	if request.method=="POST":
		nomUsuario=request.POST["username"]
		contrasenia=request.POST["password"]
		query=Usuario.objects.filter(usuario=nomUsuario)
		if query:
			usuario=Usuario.objects.get(usuario=nomUsuario)
			if (usuario.contrasenia==contrasenia):
				cliente=Cliente.objects.get(usuario=usuario)
				query=Proveedor.objects.filter(cliente=cliente)
				if query:
					return render(request,'Proveedor.html',{'nombre':cliente.nombre})
				return render(request,'Cliente.html')
		return render(request,'auth.html')	