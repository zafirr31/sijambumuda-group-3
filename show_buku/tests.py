from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from show_buku.apps import ShowBukuConfig
from django.apps import apps

from .views import buku
from .models import Buku

class LandingPage(TestCase):

    def test_show_buku_url_ada(self):
        response = Client().get('/buku/')
        self.assertEqual(response.status_code, 200)

    def test_show_buku_fungsi_show_buku(self):
        found = resolve('/buku/')
        self.assertEqual(found.func, buku)

    def test_show_buku_isi_html(self):
        request = HttpRequest()
        response = buku(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Daftar Buku', html_response)

    def test_book_models_created(self):
        dummy_book = Buku.objects.create(
            nomor_buku = 1,
            judul_buku = "Sapiens",
            pengarang = "Yuval Noah Harari",
            kategori = "Ilmiah",
            penerbit = "Gramed",
            cover = "image.jpg",
            sinopsis = "Sinopsis : Di Sapiens, Dr Yuval Noah Harari mencakup seluruh sejarah manusia, dari manusia pertama yang berjalan di bumi hingga terobosan radikal - dan terkadang menghancurkan - Revolusi Kognitif, Pertanian, dan Ilmiah"
        )
        total_buku = Buku.objects.all().count()
        self.assertEqual(total_buku, 1)
        request = HttpRequest()
        response = buku(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Sapiens', html_response)

class ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ShowBukuConfig.name, 'show_buku')
        self.assertEqual(apps.get_app_config('show_buku').name, 'show_buku')