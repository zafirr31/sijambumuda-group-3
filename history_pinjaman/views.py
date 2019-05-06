from django.shortcuts import render
from shafiya_pinjam.models import PinjamModel
from show_buku.models import Buku
from form_anggota.models import Member, Profile
from .forms import ProfileForm
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
# @login_required

def show_history(request):
    if request.user.is_authenticated:
        username = request.user.username
        member = Member.objects.get(username=username)
        if Profile.objects.filter(member=member).exists():
            profile = Profile.objects.get(member=member)
            return render(request, 'history.html', {'profile':profile, 'username':username})
        else :
            return render(request, 'history.html')
    return HttpResponseRedirect("/login/")

def history_json(request):
    if request.user.is_authenticated:
        username = request.user.username
        db_pinjam = PinjamModel.objects.filter(username=username)
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

def profile(request):
    if request.session.has_key("username"):
        if request.method == "POST" :
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid() :
                member = Member.objects.get(username=request.session["username"])
                propic = request.FILES['profile_picture']
                address = form.cleaned_data["alamat_rumah"]
                if Profile.objects.filter(member=member).exists() :
                    query = Profile.objects.get(member=member)
                    query.delete()
                profile = Profile(member=member, profile_picture=propic, alamat_rumah=address)
                profile.save()
                return HttpResponseRedirect("/history/")
        else :
            form = ProfileForm()
        return render(request, "proform.html", {"form": form})
    return HttpResponseRedirect("/login/")