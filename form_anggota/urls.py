from django.urls import path
from .views import *

urlpatterns = [
    path('registrasi-member', registrasi_member, name = "form_anggota"),
]
