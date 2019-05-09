from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from shafiya_pinjam.apps import ShafiyaPinjamConfig
from django.apps import apps
from django.contrib.auth.models import User

from .views import *
from .models import PinjamModel
from .forms import PinjamForm
import datetime


class SampleTest(TestCase):

    def test_form_pinjam_using_index_func(self):
        found = resolve('/form-pinjam/')
        self.assertEqual(found.func, pinjam)

    def test_pinjam_models_created(self):
        time = datetime.datetime.now()
        dummy_pinjam = PinjamModel.objects.create(
            username="shafiya123",
            email="shafiya123@gmail.com",
            nomor_buku="1",
            tanggal_pinjam=time,
        )
        total_pinjam = PinjamModel.objects.all().count()
        self.assertEqual(total_pinjam, 1)

    def test_form_nobuku_validated(self):
        form = PinjamForm(data={'nomor_buku': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['nomor_buku'],
            ['This field is required.']
        )

    def test_buku_no_kuota(self):
        User.objects.create_user(
            'test123', 'test@test.com', 'TestPassword123', first_name="Test")
        buku = Buku.objects.create(
            nomor_buku=1,
            judul_buku="Test Judul",
            pengarang="Test Pengarang",
            kategori="Test Kategori",
            penerbit="Test Penerbit",
            sinopsis="Test Sinopsis",
            kuota=0,
        )
        test_client = Client()
        test_client.login(username="test123", password="TestPassword123")
        test_client.post('/form-pinjam/', {'nomor_buku': 1})
        response = test_client.get('/datapeminjaman/')
        self.assertNotIn('Test Judul', response.content.decode('utf-8'))

    def test_not_logged_in(self):
        User.objects.create_user(
            'test123', 'test@test.com', 'TestPassword123', first_name="Test")
        buku = Buku.objects.create(
            nomor_buku=1,
            judul_buku="Test Judul",
            pengarang="Test Pengarang",
            kategori="Test Kategori",
            penerbit="Test Penerbit",
            sinopsis="Test Sinopsis",
            kuota=0,
        )
        test_client = Client()
        response = test_client.post('/form-pinjam/', {'nomor_buku': 1})

    def test_with_get(self):
        User.objects.create_user(
            'test123', 'test@test.com', 'TestPassword123', first_name="Test")
        buku = Buku.objects.create(
            nomor_buku=1,
            judul_buku="Test Judul",
            pengarang="Test Pengarang",
            kategori="Test Kategori",
            penerbit="Test Penerbit",
            sinopsis="Test Sinopsis",
            kuota=0,
        )
        test_client = Client()
        test_client.login(username="test123", password="TestPassword123")
        response = test_client.get('/form-pinjam/', {'nomor_buku': 1})
        self.assertIn("Peminjaman Buku", response.content.decode('utf-8'))


class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ShafiyaPinjamConfig.name, 'shafiya_pinjam')
        self.assertEqual(apps.get_app_config(
            'shafiya_pinjam').name, 'shafiya_pinjam')
