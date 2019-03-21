from .views import buku
from django.urls import path

urlpatterns = [
    path('', buku, name='buku'),
]
