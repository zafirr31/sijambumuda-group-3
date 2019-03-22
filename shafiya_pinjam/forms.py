from django import forms
from .models import PinjamModel
from form_anggota.models import Member
from show_buku.models import Buku

class PinjamForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'required':'True',
        'placeholder':'Username Anda',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'required':'True',
        'placeholder':'Email Anda',
    }))
    nomor_buku = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'required':'True',
    }))

    def clean(self):
        cleaned_data = super(PinjamForm, self).clean()
        check_username = cleaned_data.get('username')
        buku = cleaned_data.get('nomor_buku')

        db_username = []
        for i in Member.objects.all().values('Username'):
            db_username.append(i['Username'])

        db_buku = []
        for i in Buku.objects.all().values('nomor_buku'):
            db_buku.append(i['nomor_buku'])            
        
        if check_username not in db_username:
            raise forms.ValidationError("Username tidak ada")
        if buku not in db_buku:
            raise forms.ValidationError("Buku tidak ada")