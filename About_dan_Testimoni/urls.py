from django.urls import path
from .views import *

urlpatterns = [
    path('', about, name = "about"),
    path('tampil/', tampilkan, name = "tampil"),
    path('buat/', create, name = 'create')
]
