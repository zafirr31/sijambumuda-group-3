from django.shortcuts import render
from .forms import DaftarMember
from .models import Member
import datetime


"""
def registrasi_member(request):
    return render(request, "form_anggota.html")
"""

def registrasi_member(request):
    if request.method == "POST":
        form = DaftarMember(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime
            post.save()
        isi = Member.objects.all()
        return render(request, 'index.html',{'form' : form, 'isi' : isi})
    else:
        form = DaftarMember()
    return render(request, 'form_anggota.html', {'form' : form})
