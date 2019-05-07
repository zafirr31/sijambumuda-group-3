from django.db import models
<<<<<<< HEAD


class Member(models.Model):

    username = models.CharField(max_length=250)
    email = models.EmailField(null=True, unique=True)
    password = models.CharField(max_length=250)


class Profile(models.Model):
    member = models.OneToOneField(
        Member,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_picture = models.ImageField()
    alamat_rumah = models.CharField(null=True, max_length=500)
=======
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(
			User,
			on_delete=models.CASCADE,
			primary_key=True,
		)
	profile_picture = models.ImageField()
	alamat_rumah = models.CharField(null=True, max_length=500)
>>>>>>> 14d9a6263ba195a8b27fe797946432f84439fe33
