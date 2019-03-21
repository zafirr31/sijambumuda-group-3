from django.shortcuts import render

# Create your views here.
def pinjam(request):
    return render(request, 'page/form-pinjam.html',{})