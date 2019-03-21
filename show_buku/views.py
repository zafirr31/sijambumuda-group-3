from django.shortcuts import render
from .models import Buku

# Create your views here.
def buku(request):
    db = Buku.objects.all()
    content = {'data_base': db}
    return render(request, "show_buku.html", content)