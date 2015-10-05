from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Service.models import Category 
class UserForm(forms.Form):
	UserName = forms.CharField()
	Pass = forms.CharField(widget=forms.PasswordInput())
	Email= forms.EmailField()
	LastName = forms.CharField()  
	FirstName = forms.CharField(required=False)
	DNI = forms.IntegerField()
	Image =  forms.ImageField()
class ServiceForm(forms.Form):
	NameService= forms.CharField()
	Category = forms.ModelChoiceField(queryset=Category.objects.all())
	DescriptionService = forms.CharField(widget = forms.Textarea)
	Phone = forms.IntegerField()
	Email= forms.EmailField(max_length= 300)
	Adress = forms.CharField(max_length= 50)
	Image = forms.ImageField()

	