from django.shortcuts import render
from .forms import *
from .models import *
from django import forms
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
			profle = Profile(
				member=member,

				)
			return HttpResponseRedirect('/')
	else:
		register_form = RegisterMember()
	return render(request, 'form_anggota.html', {'register_form' : register_form})

def login_member(request):

	def set_cookie(login_data):
		# Set current session cookie
		# Cookie is based on username
		login = {'username': ""}
		if Member.objects.filter(username=login_data['username'][0]).exists():
			login = Member.objects.filter(username=login_data['username'][0]).values()[0]
		elif Member.objects.filter(email=login_data['username'][0]).exists():
			login = Member.objects.filter(email=login_data['username'][0]).values()[0]

		request.session['username'] = login['username']

	def validate(login_data):
		# Check's password, safe, hash and salt
		login = {'password': ""}
		if Member.objects.filter(username=login_data['username'][0]).exists():
			login = Member.objects.filter(username=login_data['username'][0]).values()[0]
		elif Member.objects.filter(email=login_data['username'][0]).exists():
			login = Member.objects.filter(email=login_data['username'][0]).values()[0]
		return check_password(login_data['password'][0], login['password'])

	if request.method == 'POST':
		login_form = LoginMember(request.POST)
		if login_form.is_valid():
			# Get post data to validate password dan set cookie
			post_data = dict(request.POST.lists())
			validation = validate(post_data)
			if(validation == True):
				set_cookie(post_data)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/login/')
	else:
		login_form = LoginMember()
	login_member_context = {'login_form': login_form}
	return render(request, 'login_member.html', login_member_context)

def logout_member(request):
	# Logout, remove session cookie
	request.session.flush()
	return HttpResponseRedirect('/')