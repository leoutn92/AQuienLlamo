from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from models import Category,Service,Comment,UserAQL
from django.template import RequestContext, loader
from django.template import RequestContext as RC
from django.utils import timezone
# Create your views here.
def Categories (request):
	category_list = {'Category':Category.objects.all()}
	return render(request,'CategoriasDjango.html',category_list)
def Cat (request,Name):
	if request.method == 'GET':
		"""return render(request,'categoriaDjango.html',suppliers_list)"""
		"""return render_to_response('categoriaDjango.html', {'suppliers':Supplier.objects.all().filter(category_id=supplier).order_by('-calificacion')},context_instance = RC( request, {} ),)"""
		return render_to_response('CategoriaDjango.html', {'Services':Service.objects.all().filter(Category=Name).order_by('-Calification')},context_instance = RC( request, {} ),)
def Serv(request,Name,NameService):
	if request.method == 'GET':
		theService = Service.objects.get(NameService=NameService)
		realComment = dict()
		comments = Comment.objects.filter(Service=theService)
		realComments = list() 
		for c in comments:
			realComment = dict()
			realComment['User'] = c.User
			realComment['Opinion']  = c.Opinion
			realComment['Image'] = realComment['User'].Image
			realComments.append(realComment)
		realComments.reverse()
		return render_to_response('Service.html', {'Service': theService,'Comments':realComments},context_instance = RC( request, {} ),)
def All(request):
	if request.method == 'GET':
		return render_to_response('AllCategories.html', {'Services':Service.objects.all().order_by('-Calification')},context_instance = RC( request, {} ),)
def New(request):
	if request.method == 'GET':
		allServices = Service.objects.all()
		today = timezone.now()
		newServices = list() 
		for a in allServices:
			if a.CreationDate.month == today.month:
				newServices.append(a)
		newServices = reversed(newServices)
		return render_to_response('NewService.html', {'Services':newServices},context_instance = RC( request, {} ),)