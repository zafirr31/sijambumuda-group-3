from django import forms
from .models import Testimoni


class IsiTestimoni(forms.Form):
        model = Testimoni
        Pesan = forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control',
            'required':'True',
            'placeholder':'Testimoni Anda',
            }))

        def clean(self):
            cleaned_data = super(IsiTestimoni, self).clean()
            check_pesan = cleaned_data.get('Pesan')
