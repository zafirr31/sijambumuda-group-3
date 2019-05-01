from django.shortcuts import render, redirect


def index(request):
    if request.session.has_key('username'):
        user = request.session['username']
    else:
        user = ""
    index_context = {'user': user}
    return render(request, "index.html", index_context)
