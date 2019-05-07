from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from show_buku.models import Buku
from .views import show_history, history_json, profile
from django.contrib.auth.models import User


class HistoryPinjamTest(TestCase):

    def test_history_url_no_login(self):
        response = Client().get('/history/')
        self.assertEqual(response.status_code, 302)

    def test_history_fungsi_show_history(self):
        found = resolve('/history/')
        self.assertEqual(found.func, show_history)

    def test_history_json_url_no_login(self):
        response = Client().get('/history/json/')
        self.assertEqual(response.status_code, 302)

    def test_history_json_fungsi_show_history(self):
        found = resolve('/history/json/')
        self.assertEqual(found.func, history_json)

    def test_logged_in(self):
        User.objects.create_user('test123', 'test@test.com', 'TestPassword123', first_name="Test")
        test_client = Client()
        test_client.login(username="test123", password="TestPassword123")
        test_client.get('/history/')
        buku = Buku.objects.create(
            nomor_buku = 1,
            judul_buku = "Test Judul",
            pengarang = "Test Pengarang",
            kategori = "Test Kategori",
            penerbit = "Test Penerbit",
            sinopsis = "Test Sinopsis",
            kuota = 1,
        )
        test_client.post('/form-pinjam/', {'nomor_buku': 1})
        test_client.get('/history/json/')

    def test_logged_in2(self):
        User.objects.create_user('test123', 'test@test.com', 'TestPassword123', first_name="Test")
        test_client = Client()
        test_client.login(username="test123", password="TestPassword123")
        test_client.get('/history/profile/')
        test_client.post('/history/profile/', {})