from django import forms
from form_anggota.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
<<<<<<< HEAD
        fields = ['profile_picture', 'alamat_rumah']
=======
        fields = ['profile_picture', 'alamat_rumah']
>>>>>>> c70cf14e65b40dae370759ed8db67a124dedf792
