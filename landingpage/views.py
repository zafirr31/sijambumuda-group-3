from django.shortcuts import render, redirect
from django.template import RequestContext


def index(request):
<<<<<<< HEAD
    if request.session.has_key('username'):
        user = request.session['username']
    else:
        user = ""
    # index_context = {'user': user}
    return render(request, "index.html")
=======
	if request.user.is_authenticated :
		user = request.user.username
	else:
		user = ""
	# index_context = {'user': user}
	return render(request, "index.html")
>>>>>>> c70cf14e65b40dae370759ed8db67a124dedf792
