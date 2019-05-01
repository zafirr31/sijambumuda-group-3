from django.shortcuts import render
from .forms import PinjamForm
from .models import PinjamModel
from form_anggota.models import Member
from show_buku.models import Buku
from django.http import HttpResponseRedirect
import datetime

# Create your views here.


def pinjam(request):
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
        request.session['email'] = request.user.email

        response.form['form'] = PinjamForm()

        if request.method == "POST":
            pinjam_form = PinjamForm(request.POST)
            if pinjam_form.is_valid():
                response['username'] = request.session['username']
                response['email'] = request.session['email']
                response['nomor_buku'] = request.POST['nomor_buku']
                response['tanggal_pinjam'] = request.POST['tanggal_pinjam']

                pinjam_model = PinjamModel(name=response['name'], email=response['email'], nomor_buku=response['nomor_buku'],
                                           tanggal_pinjam=response['tanggal_pinjam'])
                pinjam_model.save()
                return HttpResponseRedirect('/')
            else:
                pinjam_form = PinjamForm()

                # if request.method == "POST":
                #     pinjam_form = PinjamForm(request.POST)
                #     if pinjam_form.is_valid():
                #         pinjam_model = PinjamModel(
                #             username=pinjam_form.cleaned_data['username'],
                #             email=pinjam_form.cleaned_data['email'],
                #             nomor_buku=pinjam_form.cleaned_data['nomor_buku'],
                #             tanggal_pinjam=datetime.datetime.now(),
                #             nama_peminjam=Member.objects.filter(
                #                 username=pinjam_form.cleaned_data['username']).values()[0]["username"],
                #             buku_dipinjam=Buku.objects.filter(
                #                 nomor_buku=pinjam_form.cleaned_data['nomor_buku']).values()[0]["judul_buku"],
                #         )
                #         pinjam_model.save()
                #         return HttpResponseRedirect('/datapeminjaman/')
                # else:
                #     pinjam_form = PinjamForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(request, 'page/form-pinjam.html', {'form': pinjam_form})
