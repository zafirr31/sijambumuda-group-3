from django import forms
from .models import Member

class DaftarMember(forms.ModelForm):
<<<<<<< HEAD
	class Meta:
		model = Member
		fields = ('Nama', 'Nomor_Identitas',
		'Username', 'Email',
		'Password','Alamat_Rumah')

	def clean(self):
		cleaned_data = super(DaftarMember, self).clean()
		username = cleaned_data.get('Username')
		db_username = []
		for i in Member.objects.all().values('Username'):
			db_username.append(i['Username'])	
		if username in db_username:
			raise forms.ValidationError("Username sudah terdaftar")
=======
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
>>>>>>> 93b7d8b92856e14f6bc95888e6e8772d3937dde6
