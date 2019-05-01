from django.db import models


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
