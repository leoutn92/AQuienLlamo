from django.shortcuts import render
from login.forms import ServiceForm
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from Service.models import UserAQL,Service,Category
from django.http import HttpResponseRedirect
class Registrarse(FormView):
	template_name = 'registrarProveedor.html'
	form_class = ServiceForm
	success_url = reverse_lazy('registrarse')
# Create your views here.
def Profile(request):
	if request.user.is_authenticated():
		return render(request,"principal.html")
	return HttpResponseRedirect("/login")
def RegisterProveedor(request):
	return render(request,"registrarProveedor.html")
def register(request):
	if request.method== "POST":
		form = ServiceForm(request.POST,request.FILES)
		if form.is_valid:
			NameService= form['NameService'].value()
			cat=form['Category'].value()
			category=Category.objects.get(Name=cat)
			DescriptionService=form['DescriptionService'].value()
			Phone=form['Phone'].value()
			EmailField=form['Email'].value()
			Adress=form['Adress'].value()
			Image=form['Image'].value()
			userAQL=UserAQL.objects.get(User=request.user)
			service=Service(NameService=NameService,Category=category,DescriptionService=DescriptionService,Phone=Phone,Email=EmailField,Adress=Adress,Image=Image,User=userAQL)
			service.save()
			print("succes")
			return HttpResponseRedirect("/profile")
	return render(request,"registrarse.html")
"""def ModifyUserProfile(request):
	if request.method== "POST":

	theUser = request.user
	if theUser.is_authenticated():
		userAQL = UserAQL.objects.filter()"""  


