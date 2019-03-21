from django.db import models

# Create your models here.
class PinjamModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    nomor_buku = models.CharField(max_length=50)
    tanggal_pinjam = models.DateField(auto_now_add=True,blank=True)