from django.shortcuts import render
from shafiya_pinjam.models import PinjamModel

def datapeminjaman(request):
	datapeminjaman_context = {"datapeminjaman": PinjamModel.objects.all().values()[::-1]}
	return render(request, "datapeminjaman.html", datapeminjaman_context)
