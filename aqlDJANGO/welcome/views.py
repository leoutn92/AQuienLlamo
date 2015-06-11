from django.shortcuts import render_to_response
def login(request):
	return render_to_response('auth.html')
def register_c(request):
	return render_to_response('registro_c.html')
