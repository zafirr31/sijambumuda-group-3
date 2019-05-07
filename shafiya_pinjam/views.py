from django.shortcuts import render
from .forms import PinjamForm
from .models import PinjamModel
from show_buku.models import Buku
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.db.models import F

# Create your views here.


def pinjam(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pinjam_form = PinjamForm(request.POST)
            if pinjam_form.is_valid():
                username = request.user.username
                # email = Member.objects.get(username=username)['email']
                nomor_buku = request.POST['nomor_buku']
                tanggal_pinjam = datetime.datetime.now()
                buku = Buku.objects.get(nomor_buku=nomor_buku)
                if buku.kuota > 0:
                    buku.kuota = F('kuota') - 1
                    buku.save()
                    pinjam_model = PinjamModel.objects.create(username=username, nomor_buku=nomor_buku,
                                                              tanggal_pinjam=tanggal_pinjam)
                    messages.success(
                        request, "Terima kasih!\n Peminjaman Anda akan segera diproses.")
                else:
                    messages.info(
                        request, "Maaf, buku habis")
                pinjam_model.save()
                return HttpResponseRedirect('/')
        else:
            pinjam_form = PinjamForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(request, 'page/form-pinjam.html', {'form': pinjam_form})
