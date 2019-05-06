from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from form_anggota.apps import FormAnggotaConfig
from django.apps import apps

from .models import *
from .views import *
from datetime import datetime

class FormAnggota(TestCase):
    def test_form_member_url_ada(self):
        response = Client().get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_username_already_exists(self):
        Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcde1ABC", "re_password": "abcde1ABC"})
        response = Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcde1ABC", "re_password": "abcde1ABC"})
        self.assertIn("Username already taken!", response.content.decode('utf-8'))

    def test_email_already_exists(self):
        Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcde1ABC", "re_password": "abcde1ABC"})
        response = Client().post("/register/", {"username": "testt", "email": "test@test.com", "password": "abcde1ABC", "re_password": "abcde1ABC"})
        self.assertIn("Email already taken!", response.content.decode('utf-8'))

    def test_password_invalid_length(self):
        response = Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcde", "re_password": "abcde"})
        self.assertIn("Password must be atleast 8 characters long!", response.content.decode('utf-8'))

    def test_password_doesnt_match(self):
        response = Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcdefgh", "re_password": "abcdefgg"})
        self.assertIn("Passwords do not match!", response.content.decode('utf-8'))

    def test_password_doesnt_contain_number(self):
        response = Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcdefgH", "re_password": "abcdefgH"})
        self.assertIn("Password must contain atleast one number!", response.content.decode('utf-8'))

    def test_password_doesnt_contain_uppercase(self):
        response = Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcdefg1", "re_password": "abcdefg1"})
        self.assertIn("Password must contain atleast one uppercase character!", response.content.decode('utf-8'))

    def test_create_user_and_see_if_user_is_made(self):
        before = jumlahMember = User.objects.all().count()
        Client().post("/register/", {"username": "test", "email": "test@test.com", "password": "abcde1ABC", "re_password": "abcde1ABC"})
        after = jumlahMember = User.objects.all().count()
        self.assertEqual(before + 1, after)
        
class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(FormAnggotaConfig.name, 'form_anggota')
        self.assertEqual(apps.get_app_config('form_anggota').name, 'form_anggota')