from django.urls import path
from .views import *

urlpatterns = [
    path('', datapeminjaman, name = "datapeminjaman"),
]
