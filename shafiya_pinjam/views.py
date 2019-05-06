from django.shortcuts import render
from .forms import PinjamForm
from .models import PinjamModel
from show_buku.models import Buku
from django.http import HttpResponseRedirect
import datetime

# Create your views here.

def pinjam(request):
    if request.method == "POST":
        pinjam_form = PinjamForm(request.POST)
        if pinjam_form.is_valid():
            print(request.session.items())
            pinjam_model = PinjamModel(
                username=request.session['username'],
                nomor_buku=pinjam_form.cleaned_data['nomor_buku'], 
                tanggal_pinjam=datetime.datetime.now(),
                nama_peminjam = Member.objects.filter(username=pinjam_form.cleaned_data['username']).values()[0]["username"],
                buku_dipinjam = Buku.objects.filter(nomor_buku=pinjam_form.cleaned_data['nomor_buku']).values()[0]["judul_buku"],
            )
            pinjam_model.save()
            return HttpResponseRedirect('/datapeminjaman/')
    else:        
        pinjam_form = PinjamForm()

    return render(request, 'page/form-pinjam.html', {'form': pinjam_form})