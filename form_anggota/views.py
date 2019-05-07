from django.shortcuts import render
from .forms import *
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import re
import datetime


def register_member(request):
	if request.method == 'POST':
		register_form = RegisterMember(request.POST)
		if register_form.is_valid():
			user = User.objects.create_user(	
				username = register_form.cleaned_data['username'],
				email	= register_form.cleaned_data['email'],
				password = register_form.cleaned_data['password'],
			)
			return HttpResponseRedirect('/login/')
	else:
		register_form = RegisterMember()
	return render(request, 'registration/register.html', {'register_form' : register_form})

def check_username(request):
	username = request.POST.get('username')
	username = re.compile(f"^{username}$")
	all_usernames = User.objects.all().values('username')
	not_taken = True
	for i in all_usernames:
		if re.search(username, i['username']):
			not_taken = False
	return HttpResponse(str(not_taken))

def check_email(request):
	email = request.POST.get('email')
	email = re.compile(f"^{email}$")
	all_emails = User.objects.all().values('email')
	not_taken = True
	for i in all_emails:
		if re.search(email, i['email']):
			not_taken = False
	return HttpResponse(str(not_taken))

def check_password(request):
	password = request.POST.get('password')
	re_password = request.POST.get('re_password')
	return HttpResponse(str(password==re_password))
