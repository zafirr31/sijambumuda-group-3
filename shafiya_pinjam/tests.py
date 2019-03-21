from django.test import TestCase
from django.test import Client
from django.urls import resolve

from .views import *


class SampleTest(TestCase):
    # test eksistensi page form pinjam
    def test_page_form_pinjam(self):
        response = Client().get('/form-pinjam/')
        self.assertEqual(response.status_code,200)

    def test_form_pinjam_using_index_func(self):
        found = resolve('/form-pinjam/')
        self.assertEqual(found.func, pinjam)

    def test_status_template_form_pinjam_used(self):
        response = Client().get('/form-pinjam/')
        self.assertTemplateUsed(response, 'page/form-pinjam.html')