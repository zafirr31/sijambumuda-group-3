from django import forms
from .models import PinjamModel
from form_anggota.models import Member
from show_buku.models import Buku


class PinjamForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': 'True',
        'placeholder': 'Username Anda',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': 'True',
        'placeholder': 'Email Anda',
    }))
    nomor_buku = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': 'True',
        'placeholder': 'Nomor Buku',
    }))
