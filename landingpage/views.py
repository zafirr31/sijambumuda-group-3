from django.shortcuts import render, redirect
from django.template import RequestContext 

def index(request):
	if request.user.is_authenticated :
		user = request.user.username
	else:
		user = ""
	# index_context = {'user': user}
	return render(request, "index.html")