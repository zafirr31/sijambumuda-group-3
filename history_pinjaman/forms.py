from django import forms
from form_anggota.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_picture', 'alamat_rumah']
