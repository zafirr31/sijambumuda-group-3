from django.shortcuts import render
from .models import *

def datapeminjaman(request):
	datapeminjaman_context = {"datapeminjaman": Peminjaman.objects.all().values()}
	return render(request, "datapeminjaman.html", datapeminjaman_context)
