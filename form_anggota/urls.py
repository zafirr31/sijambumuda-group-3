from django.urls import path
from .views import *

urlpatterns = [
    path('', registrasi_member, name = "form_anggota"),
]
