from django.db import models

# Create your models here.
class PinjamModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    nomor_buku = models.IntegerField()
    tanggal_pinjam = models.DateField(auto_now_add=True, blank=True)
    nama_peminjam = models.CharField(max_length=100)
    buku_dipinjam = models.CharField(max_length=100)