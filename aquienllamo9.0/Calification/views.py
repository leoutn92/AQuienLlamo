from django.shortcuts import render,render_to_response
from Service.models import Service,UserAQL,Calification,Category
from django.template import RequestContext as RC
from django.http import HttpResponseRedirect
# Create your views here.
def ShowCal(service):
	califications = Calification.objects.filter(Service=service)
	prom=0
	for calif in califications:
		prom = prom + calif.Value
	prom = prom/len(califications)
	return prom
def Calificar (request,NameService):
	if request.method == 'GET':
		if request.user.is_authenticated():
			NameService1=NameService.split("/")
			cal=request.GET.get('Cal')
			if cal!=None:
				print('in')
				nameService = NameService1[0]
				service=Service.objects.get(NameService=nameService)
				user = request.user
				useraql = UserAQL.objects.get(User=user)
				value = cal
				calification = Calification(Service=service,User=useraql,Value=value)
				calification.save()
				prom = ShowCal(service)
				service.Calification = prom
				service.save()
				cat = service.Category.Name
				return HttpResponseRedirect('/categories/'+cat+'/'+nameService)
			return render_to_response('CalificationWithLogin.html',{'Services':Service.objects.all().filter(NameService=NameService1[0])},context_instance = RC( request, {} ),)
	return render_to_response('CalificationWithoutLogin.html', {'Services':Service.objects.all().filter(NameService=NameService)},context_instance = RC( request, {} ),)
def RegC(request,NameService):
	if request.method == 'GET':
		service=Service.objects.get(NameService=NameService)
		service.Calification = request.GET['Cal']
		service.save()