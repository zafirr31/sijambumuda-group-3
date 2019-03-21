from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .models import Member
from datetime import datetime
from .views import *

class FormAnggota(TestCase):

    def test_form_member_url_ada(self):
        response = Client().get('/registrasi-member')
        self.assertEqual(response.status_code, 200)

    def test_form_member_fungsi_index(self):
        found = resolve('/registrasi-member')
        self.assertEqual(found.func, registrasi_member)

    def test_form_member_isi_html(self):
        request = HttpRequest()
        response = registrasi_member(request)
        html_response = response.content.decode('utf8')
        self.assertIn('Registrasi Anggota', html_response)

    def test_poststatus_model_registrasi_member(self):
        testMember = Member.objects.create(
        Nama = "Rendya Yuschak",
        Nomor_Identitas = "1806205262",
        Username  = "Haskucy",
        Email = "rendyayuschak@gmail.com",
        Password = "siapatahu?",
        Alamat_Rumah = "Jalan Kotabaru no 15, Jakarta Pusat, Jakarta, 10150",
        )

        jumlahMember = Member.objects.all().count()
        self.assertEqual(jumlahMember, 1 )
