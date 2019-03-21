from django import forms
from .models import PinjamModel
from form_anggota.models import Member

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

    def clean_username(self):
        username = self.cleaned_data['username']
        db = Member.objects.all().values('Username').first()['Username']
        
        if username not in db:
            raise forms.ValidationError("Username tidak ada")