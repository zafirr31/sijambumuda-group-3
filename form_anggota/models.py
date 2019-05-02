from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(
			User,
			on_delete=models.CASCADE,
			primary_key=True,
		)
	profile_picture = models.ImageField()
	alamat_rumah = models.CharField(null=True, max_length=500)