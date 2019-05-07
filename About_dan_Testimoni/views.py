from django.shortcuts import render
import datetime
from .models import Testimoni
from .forms import IsiTestimoni
from django.http import HttpResponseRedirect

def about(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formTestimoni = IsiTestimoni(request.POST)
            if formTestimoni.is_valid():
                model_testimoni = Testimoni(
                Username = request.user.username,
                Pesan = formTestimoni.cleaned_data['Pesan'],
                Tanggal_Pesan = datetime.datetime.now()
                )
                model_testimoni.save()
                isi = Testimoni.objects.all()
                return HttpResponseRedirect('/about-dan-testimoni/')

        formTestimoni = IsiTestimoni()
        isi = Testimoni.objects.all()
        return render(request, 'about_dan_testimoni.html', {'form' : formTestimoni, 'isi' : isi})

    isi = Testimoni.objects.all()
    return render(request, 'about_dan_testimoni.html', {'isi' : isi})
