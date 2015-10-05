from django.shortcuts import render,render_to_response
from Service.models import Category,Service,Comment,UserAQL
from django.http import HttpResponseRedirect
from django.template import RequestContext as RC
# Create your views here.
def Com(request,Name,NameService):
	url="/categories/"+Name+"/"+NameService+"/"
	if request.method == 'POST':
		url="/categories/"+Name+"/"+NameService+"/"
		if request.user.is_authenticated():
			userAQL = UserAQL.objects.get(User=request.user)
			service = Service.objects.get(NameService=NameService)
			opinion = request.POST["Comment"]
			comment = Comment(Service=service,User=userAQL,Opinion=opinion) 
			comment.save()
			return HttpResponseRedirect(url) 						
	return render_to_response("CommentWithoutLogin.html",{'Service': NameService,'URL':url},context_instance = RC( request, {} ),)