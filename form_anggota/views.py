from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, JsonResponse
import datetime

def register_member(request):
	if request.method == 'POST':
		register_form = RegisterMember(request.POST)
		if register_form.is_valid():
			member = Member(
				username = register_form.cleaned_data['username'],
				email	= register_form.cleaned_data['email'],
				password = make_password(register_form.cleaned_data['password']),
			)
			member.save()
			return HttpResponseRedirect('/')
	else:
		register_form = RegisterMember()
	return render(request, 'form_anggota.html', {'register_form' : register_form})

def login_member(request):

	def set_cookie(login_data):
		# Set current session cookie
		# Cookie is based on username
		login = Member.objects.filter(username=login_data['username'][0]).values()[0]
		request.session['username'] = login['username']

	def validate(login_data):
		# Check's password, safe, hash and salt
		login = Member.objects.filter(username=login_data['username'][0]).values()[0]
		return check_password(login_data['password'][0], login['password'])

	if request.method == 'POST':
		login_form = LoginMember(request.POST)
		if login_form.is_valid():
			post_data = dict(request.POST.lists())
			validation = validate(post_data)
			if(validation == True):
				set_cookie(post_data)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/')
	else:
		login_form = LoginMember()
	login_member_context = {'login_form': login_form}
	return render(request, 'login_member.html', login_member_context)