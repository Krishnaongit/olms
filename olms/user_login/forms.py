from django import forms
from django.contrib.auth.models import User
from .models import Employee

class loginform(forms.Form):
	username=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'password'}))


# for registration purpose
# reference http://www.tangowithdjango.com/book17/chapters/login.html

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

class UserprofileForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('department','Tflag')