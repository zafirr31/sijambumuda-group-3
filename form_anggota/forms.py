from django import forms
from .models import *

class DaftarMember(forms.Form):

	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(min_length=8, widget=forms.PasswordInput())
	re_password = forms.CharField(min_length=8, widget=forms.PasswordInput())
