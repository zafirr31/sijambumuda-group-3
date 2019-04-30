from django.shortcuts import render

# Create your views here.
def show_history(request):
    return render(request, 'history.html')