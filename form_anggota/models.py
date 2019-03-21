from django.db import models

class Member(models.Model):
    Nama = models.CharField(max_length=250, primary_key=True)
    Nomor_Identitas = models.CharField(max_length=100)
    Username = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)
    Alamat_Rumah = models.CharField(max_length=500)
