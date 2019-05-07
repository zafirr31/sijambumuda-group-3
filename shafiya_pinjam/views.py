from django.shortcuts import render
from .forms import PinjamForm
from .models import PinjamModel
from show_buku.models import Buku
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages

# Create your views here.


def pinjam(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            pinjam_form = PinjamForm(request.POST)
            if pinjam_form.is_valid():
                username = request.session['username']
                # email = Member.objects.get(username=username)['email']
                nomor_buku = request.POST['nomor_buku']
                tanggal_pinjam = datetime.datetime.now()

                pinjam_model = PinjamModel.objects.create(username=username, nomor_buku=nomor_buku,
                                                          tanggal_pinjam=tanggal_pinjam)
                pinjam_model.save()
                messages.success(
                    request, "Terima kasih!\n Peminjaman Anda akan segera diproses.")
                return HttpResponseRedirect('/')
        else:
            pinjam_form = PinjamForm(request.POST)
    else:
        return HttpResponseRedirect('/login/')
    return render(request, 'page/form-pinjam.html', {'form': pinjam_form})
