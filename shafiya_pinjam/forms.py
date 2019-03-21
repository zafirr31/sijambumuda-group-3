from django import forms
from .models import PinjamModel

class PinjamForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form',
        'required':'True',
        'placeholder':'Username Anda',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form',
        'required':'True',
        'placeholder':'Email Anda',
    }))
    nomor_buku = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form',
        'required':'True',
    }))
    tanggal_pinjam= forms.DateField(widget=forms.TextInput(attrs={
        'class':'form',
        'required':'True',
        'placeholder':'Tanggal Pinjam?',
    }))