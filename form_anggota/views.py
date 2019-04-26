from django.shortcuts import render
from .forms import DaftarMember
from .models import *
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, JsonResponse
import datetime

def registrasi_member(request):
    if request.method == 'POST':
        register_form = DaftarMember(request.POST)
        if register_form.is_valid():
            member = Member(
                    username = register_form.cleaned_data['username'],
                    email   = register_form.cleaned_data['email'],
                    password = make_password(register_form.cleaned_data['password']),
                )
            member.save()
            return HttpResponseRedirect('/')
    else:
        register_form = DaftarMember()
    return render(request, 'form_anggota.html', {'register_form' : register_form})