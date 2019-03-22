from django import forms
from .models import Member

class DaftarMember(forms.ModelForm):
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
