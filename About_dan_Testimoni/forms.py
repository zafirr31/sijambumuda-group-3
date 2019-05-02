from django import forms
from .models import Testimoni


class IsiTestimoni(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = ('Pesan',)
