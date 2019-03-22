from django.db import models

# Create your models here.
class Buku(models.Model):
    nomor_buku = models.IntegerField()
    judul_buku = models.CharField(max_length=50)
    pengarang = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    cover = models.ImageField(upload_to="gallery", blank=True)
    sinopsis = models.TextField()