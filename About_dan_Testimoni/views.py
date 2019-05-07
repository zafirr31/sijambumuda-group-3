from django.shortcuts import render
import datetime
from .models import Testimoni
from .forms import IsiTestimoni
from django.http import HttpResponseRedirect, JsonResponse

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
                return HttpResponseRedirect('/about-dan-testimoni/')

        formTestimoni = IsiTestimoni()
        return render(request, 'about_dan_testimoni.html', {'form' : formTestimoni})

def tampilkan(request):
    isiTestimoni = Testimoni.objects.all()
    listTestimoni = []

    for data in isiTestimoni :
        listTestimoni.append({"Username" : data.Username, "Pesan" : data.Pesan, "Tanggal_Pesan" : data.Tanggal_Pesan})

    return JsonResponse(listTestimoni, safe=False)
