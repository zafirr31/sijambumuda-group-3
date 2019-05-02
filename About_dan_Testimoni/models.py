from django.db import models

class Testimoni(models.Model):
    Username = models.CharField(max_length=250)
    Pesan = models.CharField(max_length=5000)

# Create your models here.
