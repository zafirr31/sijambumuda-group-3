from django.shortcuts import render
import datetime
from .models import Testimoni
from .forms import IsiTestimoni

def about(request):
    if request.method == 'POST':
        formTestimoni = IsiTestimoni(request.POST)
        post = formTestimoni.save(commit=False)
        post.save()
        isi = Testimoni.objects.all()
        return render(request, 'about_dan_testimoni.html', {'form' : formTestimoni, 'isi' : isi})
    else:
        formTestimoni = IsiTestimoni()
        isi = " "
    return render(request, 'about_dan_testimoni.html', {'form' : formTestimoni})


    #return render(request,'about_dan_testimoni.html')


# Create your views here.
