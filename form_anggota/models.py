from django.db import models

class Member(models.Model):

	username = models.CharField(max_length=250)
	email = models.EmailField(null=True, blank=True, unique=True)
	password = models.CharField(max_length=250)

class Profile(models.Model):
	user = models.OneToOneField(
			Member,
			on_delete=models.CASCADE,
			primary_key=True,
		)
	nomor_identitas = models.CharField(max_length=100)
	alamat_rumah = models.CharField(max_length=500)