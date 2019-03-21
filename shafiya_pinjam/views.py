from django.shortcuts import render
from .forms import PinjamForm
from .models import PinjamModel
from django.http import HttpResponseRedirect

# Create your views here.

def pinjam(request):
    if request.method == "POST":
        pinjam_form = PinjamForm(request.POST)
        if pinjam_form.is_valid():
            pinjam_form.save()
            return HttpResponseRedirect('/buku')
    else:        
        pinjam_form = PinjamForm()

    return render(request, 'page/form-pinjam.html', {'form': pinjam_form})

def form_borrow(request):
    return render(request, 'page/form-pinjam.html')