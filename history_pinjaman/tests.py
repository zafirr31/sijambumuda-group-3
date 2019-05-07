from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import show_history
# Create your tests here.


class HistoryPinjamTest(TestCase):

    # def test_history_url_ada(self):
    #     response = Client().get('/history/')
    #     self.assertEqual(response.status_code, 200)

    def test_history_fungsi_show_history(self):
        found = resolve('/history/')
        self.assertEqual(found.func, show_history)

    # def test_history_isi_html(self):
    #     request = HttpRequest()
    #     response = show_history(request)
    #     html_response = response.content.decode('utf8')
    #     self.assertIn('Daftar Buku Yang Dipinjam', html_response)
