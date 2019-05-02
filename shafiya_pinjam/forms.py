from django import forms
from .models import PinjamModel
from form_anggota.models import Member
from show_buku.models import Buku

class PinjamForm(forms.Form):
    nomor_buku = forms.IntegerField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'required':'True',
        'placeholder':'Nomor Buku',
    }))

    def clean(self):
        cleaned_data = super(PinjamForm, self).clean()
        buku = cleaned_data.get('nomor_buku')

        db_buku = []
        for i in Buku.objects.all().values('nomor_buku'):
            db_buku.append(i['nomor_buku'])            
        
        if buku not in db_buku:
            raise forms.ValidationError("Buku tidak ada")