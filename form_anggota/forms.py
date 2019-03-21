from django import forms
from .models import Member

class DaftarMember(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('Nama', 'Nomor_Identitas',
        'Username', 'Email',
        'Password','Alamat_Rumah')
