from django.test import TestCase
from django.test import Client
from data_peminjaman.apps import DataPeminjamanConfig
from django.apps import apps
from django.contrib.auth.models import User

from shafiya_pinjam.models import PinjamModel
from show_buku.models import Buku
import datetime

class DataPage(TestCase):

    def test_data_page_add(self):
        time = datetime.datetime.now()
        before = PinjamModel.objects.all().count()
        buku = Buku.objects.create(
            nomor_buku = "4",
            judul_buku = "Test Judul",
            pengarang = "Test Pengarang",
            kategori = "Test Kategori",
            penerbit = "Test Penerbit",
            sinopsis = "Test Sinopsis",
        )
        peminjaman = PinjamModel.objects.create(
            nomor_buku = "4",
            tanggal_pinjam = time,
            nama_peminjam = "Test Nama",
            buku_dipinjam = "Test Judul",
        )
        after = PinjamModel.objects.all().count()
        self.assertEqual(before + 1, after)

    def test_login(self):
        User.objects.create_user('test123', 'test@test.com', 'TestPassword123', first_name="Test")
        buku = Buku.objects.create(
            nomor_buku = 1,
            judul_buku = "Test Judul",
            pengarang = "Test Pengarang",
            kategori = "Test Kategori",
            penerbit = "Test Penerbit",
            sinopsis = "Test Sinopsis",
            kuota = 1,
        )
        test_client = Client()
        test_client.login(username="test123", password="TestPassword123")
        test_client.post('/form-pinjam/', {'nomor_buku': 1})
        response = test_client.get('/datapeminjaman/')
        self.assertIn('test123', response.content.decode('utf-8'))

class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(DataPeminjamanConfig.name, 'data_peminjaman')
        self.assertEqual(apps.get_app_config('data_peminjaman').name, 'data_peminjaman')