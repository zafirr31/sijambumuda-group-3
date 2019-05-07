from django.shortcuts import render
import datetime
from .models import Testimoni
from .forms import IsiTestimoni
from django.http import HttpResponseRedirect, JsonResponse

def about(request):
    if request.user.is_authenticated:
        formTestimoni = IsiTestimoni()
        return render(request, 'about_dan_testimoni.html', {'form' : formTestimoni})
    return render(request, 'about_dan_testimoni.html')

def tampilkan(request):
    isiTestimoni = Testimoni.objects.all()
    listTestimoni = []

    for data in isiTestimoni :
        listTestimoni.append({"Username" : data.Username, "Pesan" : data.Pesan, "Tanggal_Pesan" : data.Tanggal_Pesan})

    return JsonResponse(listTestimoni, safe=False)

def create(request):
    if request.method == "POST":
        username = request.user.username
        pesan = request.POST["pesan"]
        tanggal_pesan = datetime.datetime.now()

        newTestimoni = Testimoni.objects.create(
            Username = username,
            Pesan = pesan,
            Tanggal_Pesan = tanggal_pesan
        )
        newTestimoni.save()
        return HttpResponseRedirect('/about-dan-testimoni/')
