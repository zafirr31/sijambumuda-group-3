from django import forms
from .models import Member

class DaftarMember(forms.ModelForm):
    Nama = forms.CharField(widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
                }
    ))

    Nomor_Identitas = forms.CharField(widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
                }
    ))

    Username = forms.CharField(widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
                }
    ))

    Email = forms.CharField(widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
                }
    ))

    Password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            "class" : "form-control",
                }
    ))

    Alamat_Rumah = forms.CharField(widget=forms.TextInput(
        attrs = {
            "class" : "form-control",
                }
    ))

    class Meta:
        model = Member
        fields = ('Nama', 'Nomor_Identitas',
        'Username', 'Email',
        'Password','Alamat_Rumah')