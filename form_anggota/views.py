from django.shortcuts import render
from .forms import *
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
import datetime


def register_member(request):
    if request.method == 'POST':
        register_form = RegisterMember(request.POST)
        if register_form.is_valid():
            user = User.objects.create_user(
                username=register_form.cleaned_data['username'],
                email=register_form.cleaned_data['email'],
                password=register_form.cleaned_data['password'],
            )
            return HttpResponseRedirect('login/')
    else:
        register_form = RegisterMember()
    return render(request, 'form_anggota.html', {'register_form': register_form})
