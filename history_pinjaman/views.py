from django.shortcuts import render
from shafiya_pinjam.models import PinjamModel
from show_buku.models import Buku
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
# @login_required


def show_history(request):
    return render(request, 'history.html')


def history_json(request):
    if request.user.is_authenticated:
        email = request.user.email
        db_pinjam = PinjamModel.objects.filter(email=email)
        # db_buku = Buku.objects.all()
        response_data = []
        for pinjam in db_pinjam:
            attr = dict()
            buku = Buku.objects.get(nomor_buku=pinjam.nomor_buku)
            attr["nomor_buku"] = buku.nomor_buku
            attr["judul_buku"] = buku.judul_buku
            attr["pengarang"] = buku.pengarang
            attr["penerbit"] = buku.penerbit
            attr["tanggal_pinjam"] = pinjam.tanggal_pinjam
            response_data.append(attr)
        return JsonResponse(response_data, safe=False)
    return HttpResponseRedirect("/")
