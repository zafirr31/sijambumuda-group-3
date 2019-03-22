from django.shortcuts import render
from shafiya_pinjam.models import PinjamModel
from form_anggota.models import Member

def datapeminjaman(request):
	datapeminjaman_context = {"datapeminjaman": PinjamModel.objects.all().values()[::-1]}
	return render(request, "datapeminjaman.html", datapeminjaman_context)
