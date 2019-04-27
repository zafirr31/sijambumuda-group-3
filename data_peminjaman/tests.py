from django.test import TestCase
from django.test import Client
from data_peminjaman.apps import DataPeminjamanConfig
from django.apps import apps

from shafiya_pinjam.models import PinjamModel
from form_anggota.models import Member
from show_buku.models import Buku
import datetime

class DataPage(TestCase):

    def test_data_page(self):
        time = datetime.datetime.now()
        buku = Buku.objects.create(
            nomor_buku = 4,
            judul_buku = "Test Judul",
            pengarang = "Test Pengarang",
            kategori = "Test Kategori",
            penerbit = "Test Penerbit",
            sinopsis = "Test Sinopsis",
        )
        member = Member.objects.create(
            username = "test",
            email = "test@test.com",
            password = "hahahahahah"
        )
        peminjaman = PinjamModel.objects.create(
            username = "test",
            email = "test@test.com",
            nomor_buku = "4",
            tanggal_pinjam = time,
            nama_peminjam = "Test Nama",
            buku_dipinjam = "Test Judul",
        )
        response = Client().get('/datapeminjaman/')
        self.assertIn("<b>Judul Buku:</b> Test Judul; <b>Peminjam:</b> Test Nama; <b>Tanggal Peminjaman:</b> " + time.strftime("%B %d, %Y"), response.content.decode('utf-8'))


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
        member = Member.objects.create(
            username = "test",
            email = "test@test.com",
            password = "hahahahahah"
        )
        peminjaman = PinjamModel.objects.create(
            username = "test",
            email = "test@test.com",
            nomor_buku = "4",
            tanggal_pinjam = time,
            nama_peminjam = "Test Nama",
            buku_dipinjam = "Test Judul",
        )
        after = PinjamModel.objects.all().count()
        self.assertEqual(before + 1, after)

class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(DataPeminjamanConfig.name, 'data_peminjaman')
        self.assertEqual(apps.get_app_config('data_peminjaman').name, 'data_peminjaman')