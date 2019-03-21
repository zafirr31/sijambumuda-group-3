from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import *
from .models import *
import datetime

class LandingPage(TestCase):

    def test_landing_page_url_ada(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_landing_page_fungsi_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_landing_page_isi_html(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Hello world', html_response)

class DataPage(TestCase):

    def test_data_page(self):
        time = datetime.datetime.now()
        peminjaman = Peminjaman.objects.create(
                book_title = "Test Title",
                borrower_name = "Test Name",
                borrow_time = time,
            )
        response = Client().get('/datapeminjaman/')
        self.assertIn("Judul Buku: Test Title; Peminjam: Test Name; Tanggal Peminjaman: " + time.strftime("%B %d, %Y") + " WIB", response.content.decode('utf-8'))


    def test_data_page_add(self):
        before = Peminjaman.objects.all().count()
        Peminjaman.objects.create(
                book_title = "Test Title",
                borrower_name = "Test Name",
                borrow_time = datetime.datetime.now()
            )
        after = Peminjaman.objects.all().count()
        self.assertEqual(before + 1, after)