from django.shortcuts import render,HttpResponseRedirect
from register.models import Usuario,Cliente,Proveedor
def validar(request):
	if request.method=="POST":
		nomUsuario=request.POST["username"]
		contrasenia=request.POST["password"]
		usuario=Usuario.objects.get(usuario=nomUsuario)
		if (usuario.contrasenia==contrasenia):
			cliente=Cliente.objects.get(usuario=usuario)
			query=Proveedor.objects.filter(cliente=cliente)
			if query:
				prov=Proveedor.objects.get(cliente=cliente)
				return render(request,'Cliente.html',{'prov':prov})
			return render(request,'Cliente.html',{'cli':cliente})